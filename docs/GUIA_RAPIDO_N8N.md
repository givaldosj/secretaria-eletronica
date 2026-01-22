# ⚡ GUIA RÁPIDO - CRIAR WORKFLOWS NO N8N

## 🎯 Objetivo
Criar 4 workflows em 30 minutos para sua secretária eletrônica funcionar 100%.

---

## ✅ PRÉ-REQUISITO

### 1. Adicionar Credenciais do Supabase

1. Acesse: https://app.n8n.cloud/credentials
2. Clique em **"+ New"**
3. Procure por **"Supabase"**
4. Preencha:
   ```
   Name: Supabase SecretariaEletronica
   Host: l1kwgyabiotfloyvhml.supabase.co
   API Key: sb_secret_HsJvIqd12EwCjVf9qPmz5A_KiuYhFb2
   ```
5. Clique em **"Save"**

✅ **Pronto! Credenciais adicionadas**

---

## 🔄 WORKFLOW 1: Vapi.ai → Supabase (5 minutos)

### Passo 1: Criar Workflow

1. Acesse: https://app.n8n.cloud
2. Clique em **"+ New Workflow"**
3. Nome: `Vapi.ai - Registrar Chamadas`

### Passo 2: Adicionar Webhook Trigger

1. Clique em **"+"** (adicionar node)
2. Procure por **"Webhook"**
3. Selecione **"Webhook"**
4. Configure:
   - **Method**: POST
   - **Path**: `vapi-chamadas`
5. Clique em **"Execute Workflow"** para gerar a URL
6. **Copie a URL** (você vai usar no Vapi.ai depois)

### Passo 3: Adicionar Node Supabase

1. Clique em **"+"** após o Webhook
2. Procure por **"Supabase"**
3. Selecione **"Supabase"**
4. Configure:
   - **Credentials**: Supabase SecretariaEletronica
   - **Operation**: Insert
   - **Table**: chamadas
   - **Columns**: Deixe em branco (auto-detect)
   - **Data**:
     ```json
     {
       "cliente_id": 1,
       "data_hora": "{{ now() }}",
       "duracao_segundos": "{{ $node.Webhook.json.duration }}",
       "transcricao": "{{ $node.Webhook.json.transcription }}",
       "resumo": "{{ $node.Webhook.json.summary }}",
       "status": "completada"
     }
     ```

### Passo 4: Salvar e Ativar

1. Clique em **"Save"** (canto superior direito)
2. Clique em **"Activate"** (para ativar o workflow)

✅ **Workflow 1 criado!**

---

## 💬 WORKFLOW 2: WhatsApp → Supabase (5 minutos)

### Passo 1: Criar Workflow

1. Clique em **"+ New Workflow"**
2. Nome: `WhatsApp - Receber Mensagens`

### Passo 2: Adicionar Webhook Trigger

1. Clique em **"+"**
2. Procure por **"Webhook"**
3. Configure:
   - **Method**: POST
   - **Path**: `whatsapp-mensagens`
4. Clique em **"Execute Workflow"** para gerar a URL
5. **Copie a URL** (você vai usar no WhatsApp depois)

### Passo 3: Adicionar Node Supabase

1. Clique em **"+"**
2. Procure por **"Supabase"**
3. Configure:
   - **Credentials**: Supabase SecretariaEletronica
   - **Operation**: Insert
   - **Table**: mensagens_whatsapp
   - **Data**:
     ```json
     {
       "cliente_id": 1,
       "conteudo": "{{ $node.Webhook.json.message }}",
       "tipo": "{{ $node.Webhook.json.type }}",
       "url_midia": "{{ $node.Webhook.json.media_url }}",
       "direcao": "entrada",
       "status": "recebida"
     }
     ```

### Passo 4: Salvar e Ativar

1. Clique em **"Save"**
2. Clique em **"Activate"**

✅ **Workflow 2 criado!**

---

## 📅 WORKFLOW 3: Agendamentos (5 minutos)

### Passo 1: Criar Workflow

1. Clique em **"+ New Workflow"**
2. Nome: `Agendamentos - Sistema Automático`

### Passo 2: Adicionar Webhook Trigger

1. Clique em **"+"**
2. Procure por **"Webhook"**
3. Configure:
   - **Method**: POST
   - **Path**: `agendar`
4. Clique em **"Execute Workflow"** para gerar a URL

### Passo 3: Adicionar Node Supabase (Insert)

1. Clique em **"+"**
2. Procure por **"Supabase"**
3. Configure:
   - **Credentials**: Supabase SecretariaEletronica
   - **Operation**: Insert
   - **Table**: agendamentos
   - **Data**:
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

### Passo 4: Salvar e Ativar

1. Clique em **"Save"**
2. Clique em **"Activate"**

✅ **Workflow 3 criado!**

---

## 🔔 WORKFLOW 4: Notificações (5 minutos)

### Passo 1: Criar Workflow

1. Clique em **"+ New Workflow"**
2. Nome: `Notificações - Alertar Técnico`

### Passo 2: Adicionar Webhook Trigger

1. Clique em **"+"**
2. Procure por **"Webhook"**
3. Configure:
   - **Method**: POST
   - **Path**: `notificar-tecnico`

### Passo 3: Adicionar Node Supabase (Insert)

1. Clique em **"+"**
2. Procure por **"Supabase"**
3. Configure:
   - **Credentials**: Supabase SecretariaEletronica
   - **Operation**: Insert
   - **Table**: chamadas
   - **Data**:
     ```json
     {
       "cliente_id": "{{ $node.Webhook.json.cliente_id }}",
       "data_hora": "{{ now() }}",
       "duracao_segundos": 0,
       "transcricao": "Notificação: {{ $node.Webhook.json.mensagem }}",
       "resumo": "{{ $node.Webhook.json.mensagem }}",
       "status": "notificacao"
     }
     ```

### Passo 4: Salvar e Ativar

1. Clique em **"Save"**
2. Clique em **"Activate"**

✅ **Workflow 4 criado!**

---

## 🧪 TESTAR OS WORKFLOWS

### Teste 1: Vapi.ai

1. Vá para o Workflow 1
2. Clique em **"Test"**
3. Envie dados de teste:
   ```json
   {
     "duration": 120,
     "transcription": "Olá, gostaria de agendar um atendimento",
     "summary": "Cliente quer agendar atendimento"
   }
   ```
4. Verifique no Supabase se registrou

### Teste 2: WhatsApp

1. Vá para o Workflow 2
2. Clique em **"Test"**
3. Envie dados de teste:
   ```json
   {
     "message": "Olá, tudo bem?",
     "type": "texto",
     "media_url": null
   }
   ```
4. Verifique no Supabase se registrou

### Teste 3: Agendamentos

1. Vá para o Workflow 3
2. Clique em **"Test"**
3. Envie dados de teste:
   ```json
   {
     "cliente_id": 1,
     "data": "2026-02-15",
     "hora": "10:00",
     "local": "Rua Rio Grande do Norte, 159",
     "servico": "Reparo de módulo ABS"
   }
   ```
4. Verifique no Supabase se registrou

---

## 🔗 CONECTAR WEBHOOKS

### No Vapi.ai

1. Acesse: https://dashboard.vapi.ai
2. Vá para **Assistants** → **Alex**
3. Procure por **Webhooks** ou **Events**
4. Adicione webhook:
   - **Evento**: Call Completed
   - **URL**: (URL do Workflow 1 que você copiou)
   - **Método**: POST
5. Salve

### No WhatsApp

1. Acesse: https://developers.facebook.com
2. Vá para seu app WhatsApp
3. Vá para **Configuration**
4. Adicione webhook:
   - **URL**: (URL do Workflow 2 que você copiou)
   - **Verify Token**: Gere um token seguro
5. Salve

---

## ✅ CHECKLIST FINAL

- [ ] Credenciais do Supabase adicionadas
- [ ] Workflow 1 criado e ativado
- [ ] Workflow 2 criado e ativado
- [ ] Workflow 3 criado e ativado
- [ ] Workflow 4 criado e ativado
- [ ] Webhooks testados
- [ ] Dados registrando no Supabase
- [ ] Webhooks conectados no Vapi.ai
- [ ] Webhooks conectados no WhatsApp

---

## 🚀 PRONTO!

Seus workflows estão 100% funcionando!

Agora você pode:
1. Fazer uma chamada de teste
2. Enviar mensagem WhatsApp de teste
3. Testar agendamento
4. Verificar dados no Supabase

---

## 📞 SUPORTE

Se tiver dúvidas:
1. Consulte: docs/CONFIGURAR_N8N.md
2. Consulte: docs/N8N_WORKFLOWS.md
3. Verifique logs em n8n → Executions

---

**Tempo total: ~30 minutos! 🎉**
