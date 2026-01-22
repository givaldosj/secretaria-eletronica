# 🚀 GUIA SUPER SIMPLES - IMPORTAR WORKFLOWS NO N8N

## ⏱️ Tempo Total: 15 minutos

---

## PASSO 1: CRIAR CREDENCIAL DO SUPABASE (5 minutos)

### 1.1 Acesse o n8n
```
https://givaldosj.app.n8n.cloud
```

### 1.2 Vá para Credentials
- Clique no menu lateral esquerdo
- Clique em **"Credentials"** (ou **"Credenciais"**)

### 1.3 Crie nova credencial
- Clique em **"+ Add Credential"** (ou **"+ Adicionar Credencial"**)
- Pesquise por **"Supabase"**
- Clique em **"Supabase API"**

### 1.4 Preencha os dados
```
Name: Supabase SecretariaEletronica
Host: https://l1kwgyabiotfloyvhml.supabase.co
Service Role Key: sb_secret_HsJvIqd12EwCjVf9qPmz5A_KiuYhFb2
```

### 1.5 Salve
- Clique em **"Save"** (ou **"Salvar"**)

✅ **Credencial criada!**

---

## PASSO 2: CRIAR WORKFLOW 1 - VAPI.AI (3 minutos)

### 2.1 Crie novo workflow
- Clique em **"Workflows"** no menu lateral
- Clique em **"+ Add Workflow"** ou **"Start from scratch"**

### 2.2 Renomeie o workflow
- Clique no nome "My workflow" no topo
- Digite: **Vapi.ai - Registrar Chamadas**

### 2.3 Adicione o Webhook
- Clique em **"Add first step"**
- Clique em **"On webhook call"**
- Configure:
  - **HTTP Method**: POST
  - **Path**: vapi-chamadas

### 2.4 Adicione o Code
- Clique no **"+"** à direita do Webhook
- Pesquise por **"Code"**
- Clique em **"Code"**
- Cole este código:

```javascript
// Extrair dados da chamada Vapi.ai
const body = $input.first().json.body || $input.first().json;

return [{
  json: {
    cliente_telefone: body.customer?.number || body.phoneNumber || 'desconhecido',
    data_hora: new Date().toISOString(),
    duracao_segundos: body.duration || body.call?.duration || 0,
    transcricao: body.transcript || body.messages?.map(m => m.content).join('\n') || '',
    resumo: body.summary || body.analysis?.summary || 'Chamada registrada',
    status: body.status || 'completed'
  }
}];
```

### 2.5 Adicione o Supabase
- Clique no **"+"** à direita do Code
- Pesquise por **"Supabase"**
- Clique em **"Supabase"**
- Configure:
  - **Credential**: Supabase SecretariaEletronica
  - **Operation**: Insert
  - **Table**: chamadas

### 2.6 Salve e Ative
- Clique em **"Save"** (canto superior direito)
- Clique em **"Inactive"** para ativar (muda para **"Active"**)

### 2.7 Copie a URL do Webhook
- Clique no node **"Webhook"**
- Clique em **"Production URL"**
- Copie a URL (ex: `https://givaldosj.app.n8n.cloud/webhook/vapi-chamadas`)

✅ **Workflow 1 criado!**

---

## PASSO 3: CRIAR WORKFLOW 2 - WHATSAPP (3 minutos)

### 3.1 Crie novo workflow
- Clique em **"Workflows"** → **"+ Add Workflow"**
- Renomeie para: **WhatsApp - Receber Mensagens**

### 3.2 Adicione o Webhook
- **HTTP Method**: POST
- **Path**: whatsapp-mensagens

### 3.3 Adicione o Code
Cole este código:

```javascript
// Extrair dados da mensagem WhatsApp
const body = $input.first().json.body || $input.first().json;

const entry = body.entry?.[0];
const changes = entry?.changes?.[0];
const value = changes?.value;
const message = value?.messages?.[0];
const contact = value?.contacts?.[0];

return [{
  json: {
    cliente_telefone: message?.from || body.from || body.phone || 'desconhecido',
    cliente_nome: contact?.profile?.name || body.name || 'Cliente',
    conteudo: message?.text?.body || message?.caption || body.message || body.text || '',
    tipo: message?.type || body.type || 'texto',
    url_midia: message?.image?.url || message?.video?.url || message?.audio?.url || body.media_url || null,
    direcao: 'entrada',
    status: 'recebida',
    criado_em: new Date().toISOString()
  }
}];
```

### 3.4 Adicione o Supabase
- **Credential**: Supabase SecretariaEletronica
- **Operation**: Insert
- **Table**: mensagens_whatsapp

### 3.5 Salve e Ative
- Copie a URL do Webhook

✅ **Workflow 2 criado!**

---

## PASSO 4: CRIAR WORKFLOW 3 - AGENDAMENTOS (3 minutos)

### 4.1 Crie novo workflow
- Renomeie para: **Agendamentos - Sistema Automático**

### 4.2 Adicione o Webhook
- **HTTP Method**: POST
- **Path**: agendar

### 4.3 Adicione o Code
Cole este código:

```javascript
// Extrair dados do agendamento
const body = $input.first().json.body || $input.first().json;

return [{
  json: {
    cliente_telefone: body.telefone || body.phone || 'desconhecido',
    cliente_nome: body.nome || body.name || 'Cliente',
    data_agendamento: body.data || body.date || new Date().toISOString().split('T')[0],
    hora_agendamento: body.hora || body.time || '09:00',
    local: body.local || body.location || 'Rua Rio Grande do Norte, 159',
    servico: body.servico || body.service || 'Atendimento geral',
    status: 'agendado',
    notas: body.notas || body.notes || '',
    criado_em: new Date().toISOString()
  }
}];
```

### 4.4 Adicione o Supabase
- **Credential**: Supabase SecretariaEletronica
- **Operation**: Insert
- **Table**: agendamentos

### 4.5 Salve e Ative
- Copie a URL do Webhook

✅ **Workflow 3 criado!**

---

## PASSO 5: CONECTAR WEBHOOKS (5 minutos)

### 5.1 Conectar Vapi.ai

1. Acesse: https://dashboard.vapi.ai
2. Vá para **Assistants** → **Alex**
3. Vá para **Advanced** → **Server URL**
4. Cole a URL do webhook Vapi.ai:
```
https://givaldosj.app.n8n.cloud/webhook/vapi-chamadas
```
5. Salve

### 5.2 Conectar WhatsApp (Evolution API ou similar)

1. Acesse seu painel do WhatsApp Business API
2. Configure o webhook para:
```
https://givaldosj.app.n8n.cloud/webhook/whatsapp-mensagens
```

---

## ✅ PRONTO!

Seu sistema agora:
- ✅ Recebe chamadas do Vapi.ai
- ✅ Registra no banco de dados
- ✅ Recebe mensagens do WhatsApp
- ✅ Gerencia agendamentos

---

## 📋 URLs DOS WEBHOOKS (COPIE)

```
Vapi.ai:      https://givaldosj.app.n8n.cloud/webhook/vapi-chamadas
WhatsApp:     https://givaldosj.app.n8n.cloud/webhook/whatsapp-mensagens
Agendamentos: https://givaldosj.app.n8n.cloud/webhook/agendar
```

---

## 🔧 TESTAR OS WORKFLOWS

### Testar Vapi.ai
```bash
curl -X POST https://givaldosj.app.n8n.cloud/webhook/vapi-chamadas \
  -H "Content-Type: application/json" \
  -d '{"phoneNumber": "79999999999", "duration": 120, "transcript": "Teste de chamada", "status": "completed"}'
```

### Testar WhatsApp
```bash
curl -X POST https://givaldosj.app.n8n.cloud/webhook/whatsapp-mensagens \
  -H "Content-Type: application/json" \
  -d '{"from": "79999999999", "name": "Cliente Teste", "message": "Olá, preciso de ajuda", "type": "texto"}'
```

### Testar Agendamentos
```bash
curl -X POST https://givaldosj.app.n8n.cloud/webhook/agendar \
  -H "Content-Type: application/json" \
  -d '{"telefone": "79999999999", "nome": "Cliente Teste", "data": "2026-01-25", "hora": "09:00", "local": "Rua Rio Grande do Norte, 159", "servico": "Reparo de módulo"}'
```

---

## 📞 SUPORTE

Se tiver dúvidas:
1. Consulte a documentação completa em `docs/DOCUMENTACAO_FINAL.md`
2. Verifique os logs no n8n (Executions)
3. Verifique os dados no Supabase (Table Editor)
