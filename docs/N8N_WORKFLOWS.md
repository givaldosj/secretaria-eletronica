# 🔄 WORKFLOWS N8N - SECRETÁRIA ELETRÔNICA

## Visão Geral

Os workflows do n8n integram:
- **Vapi.ai** → Registrar chamadas no Supabase
- **WhatsApp** → Receber e armazenar mensagens
- **Agendamentos** → Sistema automático
- **Notificações** → Alertar técnico

---

## WORKFLOW 1: Vapi.ai → Supabase (Registrar Chamadas)

### Objetivo
Quando uma chamada termina no Vapi.ai, registrar os dados no banco de dados.

### Fluxo
```
Vapi.ai Webhook
    ↓
Extrair dados da chamada
    ↓
Buscar cliente por telefone
    ↓
Registrar chamada no Supabase
    ↓
Enviar confirmação
```

### Dados capturados
- Telefone do cliente
- Data e hora da chamada
- Duração
- Transcrição
- Resumo da conversa
- Status (completada, perdida, transferida)

### Configuração no n8n

**1. Webhook Trigger**
- Tipo: Webhook
- Método: POST
- URL: `https://seu-n8n.com/webhook/vapi-chamadas`

**2. Extrair dados**
- Node: Function
- Extrair: telefone, duracao, transcricao, resumo, status

**3. Buscar cliente**
- Node: Supabase
- Operação: Select
- Tabela: clientes
- Filtro: telefone = {{$node.Extract.data.telefone}}

**4. Registrar chamada**
- Node: Supabase
- Operação: Insert
- Tabela: chamadas
- Dados:
  ```json
  {
    "cliente_id": "{{$node.BuscarCliente.data[0].id}}",
    "data_hora": "{{now()}}",
    "duracao_segundos": "{{$node.Extract.data.duracao}}",
    "transcricao": "{{$node.Extract.data.transcricao}}",
    "resumo": "{{$node.Extract.data.resumo}}",
    "status": "{{$node.Extract.data.status}}"
  }
  ```

---

## WORKFLOW 2: WhatsApp → Supabase (Receber Mensagens)

### Objetivo
Quando receber uma mensagem no WhatsApp, armazenar no banco.

### Fluxo
```
WhatsApp Webhook
    ↓
Extrair dados da mensagem
    ↓
Verificar tipo (texto/imagem/video)
    ↓
Se imagem/video: Fazer upload para S3
    ↓
Buscar cliente por telefone
    ↓
Registrar mensagem no Supabase
    ↓
Responder com mensagem automática
```

### Dados capturados
- Telefone do remetente
- Conteúdo da mensagem
- Tipo (texto, imagem, vídeo, áudio)
- URL da mídia (se houver)
- Timestamp

### Configuração no n8n

**1. Webhook Trigger**
- Tipo: Webhook
- Método: POST
- URL: `https://seu-n8n.com/webhook/whatsapp-mensagens`

**2. Extrair dados**
- Node: Function
- Extrair: telefone, conteudo, tipo, url_midia

**3. Condicional: Tipo de mídia**
- Se tipo = imagem/video:
  - Node: S3 (Upload)
  - Salvar arquivo
  - Obter URL pública

**4. Buscar cliente**
- Node: Supabase
- Operação: Select
- Tabela: clientes
- Filtro: telefone = {{$node.Extract.data.telefone}}

**5. Registrar mensagem**
- Node: Supabase
- Operação: Insert
- Tabela: mensagens_whatsapp
- Dados:
  ```json
  {
    "cliente_id": "{{$node.BuscarCliente.data[0].id}}",
    "conteudo": "{{$node.Extract.data.conteudo}}",
    "tipo": "{{$node.Extract.data.tipo}}",
    "url_midia": "{{$node.S3Upload.data.url}}",
    "direcao": "entrada",
    "status": "recebida"
  }
  ```

**6. Responder automaticamente**
- Node: WhatsApp
- Mensagem: "Olá! Recebemos sua mensagem. Um técnico responderá em breve."

---

## WORKFLOW 3: Sistema de Agendamentos

### Objetivo
Permitir que clientes agendem atendimento via WhatsApp ou voz.

### Fluxo
```
Cliente solicita agendamento
    ↓
Extrair data e hora desejada
    ↓
Verificar disponibilidade
    ↓
Criar agendamento
    ↓
Enviar confirmação
    ↓
Agendar lembrete
```

### Configuração no n8n

**1. Trigger: Palavra-chave no WhatsApp**
- Detectar: "agendar", "agendamento", "marcar"

**2. Extrair informações**
- Node: OpenAI (ou similar)
- Extrair: data desejada, horário, local preferido

**3. Verificar disponibilidade**
- Node: Supabase
- Operação: Select
- Tabela: agendamentos
- Filtro: data_agendamento = {{data}} AND hora_agendamento = {{hora}}
- Se existir: Sugerir outro horário

**4. Criar agendamento**
- Node: Supabase
- Operação: Insert
- Tabela: agendamentos
- Dados:
  ```json
  {
    "cliente_id": "{{cliente_id}}",
    "data_agendamento": "{{data}}",
    "hora_agendamento": "{{hora}}",
    "local": "{{local}}",
    "servico": "{{servico}}",
    "status": "agendado"
  }
  ```

**5. Enviar confirmação**
- Node: WhatsApp
- Mensagem: "Agendamento confirmado para {{data}} às {{hora}} em {{local}}"

**6. Agendar lembrete**
- Node: Schedule
- Executar 24 horas antes
- Enviar mensagem de lembrete

---

## WORKFLOW 4: Notificações ao Técnico

### Objetivo
Alertar o técnico sobre chamadas e agendamentos.

### Fluxo
```
Nova chamada registrada
    ↓
Verificar horário de atendimento
    ↓
Se fora do horário: Notificar técnico
    ↓
Se dentro do horário: Enviar para fila
```

### Configuração no n8n

**1. Trigger: Nova chamada**
- Node: Supabase
- Operação: Watch
- Tabela: chamadas

**2. Verificar horário**
- Node: Function
- Comparar hora atual com horários de atendimento
- Se fora do horário: Notificar

**3. Enviar notificação**
- Node: WhatsApp / Email / Telegram
- Mensagem: "Nova chamada de {{cliente_nome}} - {{telefone}}"
- Incluir: Resumo da chamada, Transcrição

---

## 🔧 CONFIGURAÇÃO DAS CREDENCIAIS NO N8N

### 1. Supabase Credentials
```
Nome: Supabase SecretariaEletronica
Tipo: HTTP Basic Auth
URL: https://l1kwgyabiotfloyvhml.supabase.co
API Key: sb_secret_HsJvIqd12EwCjVf9qPmz5A_KiuYhFb2
```

### 2. Vapi.ai Credentials
```
Nome: Vapi.ai
Tipo: API Key
API Key: [Sua chave do Vapi.ai]
```

### 3. WhatsApp Credentials
```
Nome: WhatsApp Business
Tipo: OAuth2
Token: [Seu token do WhatsApp]
Phone Number ID: [Seu ID]
```

### 4. Twilio Credentials (se necessário)
```
Nome: Twilio
Tipo: API Key
Account SID: [Seu SID]
Auth Token: [Seu token]
```

---

## 📝 VARIÁVEIS DE AMBIENTE

Adicionar no n8n:
```
SUPABASE_URL=https://l1kwgyabiotfloyvhml.supabase.co
SUPABASE_ANON_KEY=sb_publishable__JDZLtnS03fPIfJuUb6nWw_HRRdVfxR
SUPABASE_SERVICE_ROLE_KEY=sb_secret_HsJvIqd12EwCjVf9qPmz5A_KiuYhFb2
VAPI_API_KEY=[Sua chave]
WHATSAPP_TOKEN=[Seu token]
TWILIO_ACCOUNT_SID=[Seu SID]
TWILIO_AUTH_TOKEN=[Seu token]
```

---

## 🧪 TESTES

### Testar Workflow 1 (Vapi.ai)
1. Fazer uma chamada de teste no Vapi.ai
2. Verificar se registrou em: Supabase → chamadas
3. Confirmar: data_hora, duracao_segundos, transcricao

### Testar Workflow 2 (WhatsApp)
1. Enviar mensagem de teste no WhatsApp
2. Verificar se registrou em: Supabase → mensagens_whatsapp
3. Confirmar: conteudo, tipo, direcao

### Testar Workflow 3 (Agendamentos)
1. Enviar "agendar" no WhatsApp
2. Seguir fluxo de agendamento
3. Verificar se criou em: Supabase → agendamentos

### Testar Workflow 4 (Notificações)
1. Simular nova chamada fora do horário
2. Verificar se técnico recebeu notificação

---

## 🚀 PRÓXIMOS PASSOS

1. **Acessar n8n**: https://n8n.cloud
2. **Criar workflows** seguindo as configurações acima
3. **Testar cada workflow**
4. **Ativar webhooks** no Vapi.ai e WhatsApp
5. **Monitorar logs** para erros

---

## 📊 MONITORAMENTO

No n8n, você pode:
- Ver histórico de execuções
- Verificar logs de erro
- Monitorar performance
- Receber alertas de falhas

---

**Tudo pronto para começar! 🚀**
