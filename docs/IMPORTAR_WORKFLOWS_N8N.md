# 📥 GUIA: IMPORTAR WORKFLOWS NO N8N

## 🎯 Objetivo
Importar 4 workflows prontos em apenas **5 minutos**!

---

## ✅ PRÉ-REQUISITO

### 1. Adicionar Credenciais do Supabase

Antes de importar, adicione as credenciais do Supabase no n8n:

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

✅ **Credenciais adicionadas!**

---

## 📥 IMPORTAR WORKFLOWS

### Passo 1: Obter o Arquivo JSON

O arquivo com os 4 workflows está em:
```
workflows/workflows_completos.json
```

### Passo 2: Copiar o Arquivo

```bash
# Copiar para a área de transferência (Linux/Mac)
cat workflows/workflows_completos.json | xclip -selection clipboard

# Ou abrir o arquivo e copiar manualmente
```

### Passo 3: Importar no n8n

1. Acesse: https://app.n8n.cloud
2. Clique em **"Workflows"** (menu lateral)
3. Clique em **"+ New"**
4. Clique em **"Import from File"** ou **"Import from URL"**
5. Cole o JSON ou selecione o arquivo
6. Clique em **"Import"**

### Passo 4: Verificar Workflows

Após importar, você verá os 4 workflows:

1. ✅ **Vapi.ai - Registrar Chamadas**
2. ✅ **WhatsApp - Receber Mensagens**
3. ✅ **Agendamentos - Sistema Automático**
4. ✅ **Notificações - Alertar Técnico**

---

## 🔧 CONFIGURAR CREDENCIAIS NOS WORKFLOWS

Após importar, você precisa conectar as credenciais:

### Para Cada Workflow:

1. Abra o workflow
2. Clique no node **"Supabase - Inserir..."**
3. Vá para **"Credentials"**
4. Selecione **"Supabase SecretariaEletronica"**
5. Clique em **"Save"**

**Repita para todos os 4 workflows**

---

## 🧪 TESTAR OS WORKFLOWS

### Teste 1: Vapi.ai

1. Abra: **Vapi.ai - Registrar Chamadas**
2. Clique em **"Test"**
3. Envie dados de teste:
   ```json
   {
     "duration": 120,
     "transcription": "Olá, gostaria de agendar um atendimento",
     "summary": "Cliente quer agendar"
   }
   ```
4. Verifique no Supabase → **chamadas**

### Teste 2: WhatsApp

1. Abra: **WhatsApp - Receber Mensagens**
2. Clique em **"Test"**
3. Envie dados de teste:
   ```json
   {
     "message": "Olá, tudo bem?",
     "type": "texto",
     "media_url": null
   }
   ```
4. Verifique no Supabase → **mensagens_whatsapp**

### Teste 3: Agendamentos

1. Abra: **Agendamentos - Sistema Automático**
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
4. Verifique no Supabase → **agendamentos**

### Teste 4: Notificações

1. Abra: **Notificações - Alertar Técnico**
2. Clique em **"Test"**
3. Envie dados de teste:
   ```json
   {
     "cliente_id": 1,
     "mensagem": "Nova chamada de João Silva"
   }
   ```
4. Verifique no Supabase → **chamadas**

---

## ✅ ATIVAR WORKFLOWS

Após testar, ative todos os workflows:

1. Para cada workflow, clique em **"Activate"** (canto superior direito)
2. Você verá um aviso: "Workflow is active"
3. Copie a **URL do webhook** que aparece

---

## 🔗 CONECTAR WEBHOOKS

### No Vapi.ai

1. Acesse: https://dashboard.vapi.ai
2. Vá para **Assistants** → **Alex**
3. Procure por **Webhooks** ou **Events**
4. Adicione webhook:
   - **Evento**: Call Completed
   - **URL**: (URL do Workflow 1)
   - **Método**: POST
5. Salve

### No WhatsApp

1. Acesse: https://developers.facebook.com
2. Vá para seu app WhatsApp
3. Vá para **Configuration**
4. Adicione webhook:
   - **URL**: (URL do Workflow 2)
   - **Verify Token**: Gere um token seguro
5. Salve

---

## 📊 MONITORAR WORKFLOWS

### Ver Execuções

1. Abra o workflow
2. Clique em **"Executions"**
3. Veja o histórico de execuções
4. Clique em uma execução para ver detalhes

### Ver Logs

1. Clique em **"Logs"**
2. Veja mensagens de erro
3. Use para debug

---

## ✅ CHECKLIST FINAL

- [ ] Credenciais do Supabase adicionadas
- [ ] Workflows importados
- [ ] Credenciais conectadas em cada workflow
- [ ] Todos os 4 workflows testados
- [ ] Todos os 4 workflows ativados
- [ ] URLs dos webhooks copiadas
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
1. Consulte: docs/GUIA_RAPIDO_N8N.md
2. Consulte: docs/N8N_WORKFLOWS.md
3. Verifique logs em n8n → Executions

---

**Tempo total: ~5 minutos para importar + ~10 minutos para testar = 15 minutos! 🎉**
