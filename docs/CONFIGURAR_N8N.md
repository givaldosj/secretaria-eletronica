# 🔧 GUIA DE CONFIGURAÇÃO N8N

## Passo 1: Acessar n8n.cloud

1. Acesse: https://n8n.cloud
2. Faça login com:
   - Email: `givaldosj@gmail.com`
   - Senha: `RvD8HeUKP4QCb4F`

---

## Passo 2: Adicionar Credenciais do Supabase

### 2.1 Vá para Credentials
- Clique em **Credentials** (cadeado) no menu superior
- Clique em **+ New**
- Selecione **Supabase**

### 2.2 Preencha os dados
```
Name: Supabase SecretariaEletronica
Host: l1kwgyabiotfloyvhml.supabase.co
API Key: sb_secret_HsJvIqd12EwCjVf9qPmz5A_KiuYhFb2
```

### 2.3 Salve
- Clique em **Save**

---

## Passo 3: Criar Workflow 1 - Vapi.ai → Supabase

### 3.1 Criar novo workflow
- Clique em **+ New Workflow**
- Nome: `Vapi.ai - Registrar Chamadas`

### 3.2 Adicionar Webhook Trigger
1. Clique em **+** para adicionar node
2. Procure por **Webhook**
3. Selecione **Webhook**
4. Configure:
   - Method: POST
   - Path: `vapi-chamadas`
   - Clique em **Execute Workflow** para gerar a URL

### 3.3 Adicionar node Supabase
1. Clique em **+** para adicionar node após o Webhook
2. Procure por **Supabase**
3. Selecione **Supabase**
4. Configure:
   - Credentials: Supabase SecretariaEletronica
   - Operation: Insert
   - Table: chamadas
   - Data:
     ```json
     {
       "cliente_id": 1,
       "data_hora": "{{ now() }}",
       "duracao_segundos": "{{ $node.Webhook.json.duracao }}",
       "transcricao": "{{ $node.Webhook.json.transcricao }}",
       "resumo": "{{ $node.Webhook.json.resumo }}",
       "status": "completada"
     }
     ```

### 3.4 Salvar e ativar
- Clique em **Save**
- Clique em **Activate** (para ativar o workflow)

---

## Passo 4: Criar Workflow 2 - WhatsApp → Supabase

### 4.1 Criar novo workflow
- Clique em **+ New Workflow**
- Nome: `WhatsApp - Receber Mensagens`

### 4.2 Adicionar Webhook Trigger
1. Clique em **+**
2. Procure por **Webhook**
3. Configure:
   - Method: POST
   - Path: `whatsapp-mensagens`

### 4.3 Adicionar node Supabase
1. Clique em **+**
2. Procure por **Supabase**
3. Configure:
   - Credentials: Supabase SecretariaEletronica
   - Operation: Insert
   - Table: mensagens_whatsapp
   - Data:
     ```json
     {
       "cliente_id": 1,
       "conteudo": "{{ $node.Webhook.json.conteudo }}",
       "tipo": "{{ $node.Webhook.json.tipo }}",
       "url_midia": "{{ $node.Webhook.json.url_midia }}",
       "direcao": "entrada",
       "status": "recebida"
     }
     ```

### 4.4 Salvar e ativar
- Clique em **Save**
- Clique em **Activate**

---

## Passo 5: Criar Workflow 3 - Agendamentos

### 5.1 Criar novo workflow
- Clique em **+ New Workflow**
- Nome: `Agendamentos - Sistema Automático`

### 5.2 Adicionar Webhook Trigger
1. Clique em **+**
2. Procure por **Webhook**
3. Configure:
   - Method: POST
   - Path: `agendar`

### 5.3 Adicionar node Supabase (Insert)
1. Clique em **+**
2. Procure por **Supabase**
3. Configure:
   - Credentials: Supabase SecretariaEletronica
   - Operation: Insert
   - Table: agendamentos
   - Data:
     ```json
     {
       "cliente_id": "{{ $node.Webhook.json.cliente_id }}",
       "data_agendamento": "{{ $node.Webhook.json.data }}",
       "hora_agendamento": "{{ $node.Webhook.json.hora }}",
       "local": "{{ $node.Webhook.json.local }}",
       "servico": "{{ $node.Webhook.json.servico }}",
       "status": "agendado"
     }
     ```

### 5.4 Salvar e ativar
- Clique em **Save**
- Clique em **Activate**

---

## Passo 6: Configurar Webhooks no Vapi.ai

### 6.1 Acessar Vapi.ai
- Acesse: https://dashboard.vapi.ai
- Vá para **Assistants**
- Selecione **Alex**

### 6.2 Adicionar Webhook
- Procure por **Webhooks** ou **Events**
- Adicione novo webhook:
  - **Evento**: Call Completed
  - **URL**: `https://seu-n8n-url.com/webhook/vapi-chamadas`
  - **Método**: POST

### 6.3 Salvar
- Clique em **Save**

---

## Passo 7: Configurar Webhooks no WhatsApp

### 7.1 Acessar WhatsApp Business
- Acesse: https://developers.facebook.com
- Vá para seu app WhatsApp

### 7.2 Adicionar Webhook
- Vá para **Configuration**
- Adicione webhook:
  - **URL**: `https://seu-n8n-url.com/webhook/whatsapp-mensagens`
  - **Verify Token**: Gere um token seguro

### 7.3 Salvar
- Clique em **Save**

---

## 🧪 TESTAR OS WORKFLOWS

### Teste 1: Vapi.ai
1. Faça uma chamada de teste no Vapi.ai
2. Verifique em n8n: **Executions** → Vapi.ai workflow
3. Verifique no Supabase: **chamadas** → deve ter novo registro

### Teste 2: WhatsApp
1. Envie uma mensagem de teste no WhatsApp
2. Verifique em n8n: **Executions** → WhatsApp workflow
3. Verifique no Supabase: **mensagens_whatsapp** → deve ter novo registro

### Teste 3: Agendamento
1. Envie um webhook de teste para agendar
2. Verifique em n8n: **Executions** → Agendamentos workflow
3. Verifique no Supabase: **agendamentos** → deve ter novo registro

---

## 📊 MONITORAR WORKFLOWS

### Ver Execuções
- Clique em **Executions** no workflow
- Veja histórico de execuções
- Clique em uma execução para ver detalhes

### Ver Logs
- Clique em **Logs** para ver mensagens de erro
- Use para debug se algo não funcionar

### Ativar/Desativar
- Clique em **Activate** para ativar
- Clique em **Deactivate** para desativar

---

## 🔐 DICAS DE SEGURANÇA

1. **Nunca compartilhe credenciais** - Guarde em lugar seguro
2. **Use HTTPS** - Todos os webhooks devem ser HTTPS
3. **Valide tokens** - Verifique tokens antes de processar
4. **Monitore logs** - Verifique regularmente por erros
5. **Faça backup** - Exporte workflows regularmente

---

## ❓ TROUBLESHOOTING

### Erro: "Supabase connection failed"
- Verifique se a URL está correta
- Verifique se a API Key está correta
- Teste a conexão clicando em "Test"

### Erro: "Webhook not receiving data"
- Verifique se o webhook está ativo (Activate)
- Verifique se a URL está correta
- Teste enviando dados manualmente

### Erro: "Table not found"
- Verifique se executou o SQL no Supabase
- Verifique se o nome da tabela está correto
- Verifique se tem permissão de acesso

---

## 📞 SUPORTE

Se tiver dúvidas:
1. Consulte a documentação do n8n: https://docs.n8n.io
2. Consulte a documentação do Supabase: https://supabase.com/docs
3. Verifique os logs de erro em n8n

---

**Tudo pronto! Seus workflows estão configurados! 🚀**
