# 📸 GUIA VISUAL - IMPORTAR WORKFLOWS EM 10 MINUTOS

## 🎯 Objetivo Rápido

Importar 4 workflows prontos no n8n em **menos de 10 minutos**!

---

## ⚡ RESUMO RÁPIDO

```
1. Abra o arquivo JSON (2 min)
2. Copie o conteúdo (1 min)
3. Vá para n8n (1 min)
4. Importe o arquivo (2 min)
5. Conecte credenciais (3 min)
6. Ative workflows (1 min)
```

**Total: ~10 minutos! ✅**

---

## 📋 PASSO 1: ABRIR ARQUIVO JSON

### Localizar o Arquivo

```
/home/ubuntu/secretaria_eletronica/workflows/workflows_completos.json
```

### Opções para Abrir:

**Opção A: Terminal (Linux/Mac)**
```bash
cat /home/ubuntu/secretaria_eletronica/workflows/workflows_completos.json
```

**Opção B: Editor de Texto**
- Abra qualquer editor (VS Code, Notepad, etc)
- Vá para File → Open
- Navegue até o arquivo
- Abra

**Opção C: GitHub**
- Acesse: https://github.com/givaldosj/secretaria-eletronica
- Vá para: workflows → workflows_completos.json
- Clique em "Raw"
- Copie tudo

---

## 📋 PASSO 2: COPIAR CONTEÚDO

### Copiar Todo o JSON

```bash
# Linux/Mac
cat workflows/workflows_completos.json | xclip -selection clipboard

# Ou manualmente:
# Ctrl+A (selecionar tudo)
# Ctrl+C (copiar)
```

✅ **Conteúdo copiado para a área de transferência!**

---

## 🌐 PASSO 3: ACESSAR N8N

### Abrir n8n

1. Acesse: https://givaldosj.app.n8n.cloud
2. Você já deve estar logado

### Navegar para Workflows

1. Procure pelo menu lateral
2. Clique em **"Workflows"** ou **"Home"**
3. Você verá a lista de workflows

---

## 📥 PASSO 4: IMPORTAR WORKFLOWS

### Opção A: Import from File (Recomendado)

1. Procure por um botão **"+"** ou **"New"**
2. Clique em **"Import from File"** ou **"Import"**
3. Uma caixa de diálogo abrirá
4. **Cole o JSON** (Ctrl+V)
5. Clique em **"Import"**

### Opção B: Import from URL

Se o arquivo estiver em URL:
1. Clique em **"Import from URL"**
2. Cole a URL do arquivo
3. Clique em **"Import"**

### Opção C: Importar Manualmente

Se não encontrar opção de import:
1. Crie cada workflow manualmente
2. Siga o guia em: `docs/GUIA_RAPIDO_N8N.md`

---

## ✅ PASSO 5: VERIFICAR WORKFLOWS IMPORTADOS

Após importar, você verá:

```
✅ Vapi.ai - Registrar Chamadas
✅ WhatsApp - Receber Mensagens
✅ Agendamentos - Sistema Automático
✅ Notificações - Alertar Técnico
```

---

## 🔧 PASSO 6: CONECTAR CREDENCIAIS

### Para Cada Workflow:

1. **Abra o workflow**
   - Clique no nome do workflow

2. **Localize o node Supabase**
   - Procure por um node chamado "Supabase - Inserir..."

3. **Conecte as credenciais**
   - Clique no node
   - Vá para **"Credentials"** ou **"Authentication"**
   - Selecione **"Supabase SecretariaEletronica"**
   - Se não existir, crie uma nova:
     - Clique em **"+ New"**
     - Nome: `Supabase SecretariaEletronica`
     - Host: `l1kwgyabiotfloyvhml.supabase.co`
     - API Key: `sb_secret_HsJvIqd12EwCjVf9qPmz5A_KiuYhFb2`
     - Clique em **"Save"**

4. **Salve o workflow**
   - Clique em **"Save"** (canto superior direito)

**Repita para os 4 workflows**

---

## 🧪 PASSO 7: TESTAR WORKFLOWS

### Teste Rápido para Cada Workflow:

**Workflow 1: Vapi.ai - Registrar Chamadas**
1. Abra o workflow
2. Clique em **"Test"** ou **"Execute"**
3. Verifique se funcionou (sem erros)

**Workflow 2: WhatsApp - Receber Mensagens**
1. Abra o workflow
2. Clique em **"Test"**
3. Verifique se funcionou

**Workflow 3: Agendamentos**
1. Abra o workflow
2. Clique em **"Test"**
3. Verifique se funcionou

**Workflow 4: Notificações**
1. Abra o workflow
2. Clique em **"Test"**
3. Verifique se funcionou

---

## 🚀 PASSO 8: ATIVAR WORKFLOWS

### Para Cada Workflow:

1. **Abra o workflow**
2. **Clique em "Activate"** (botão no canto superior direito)
3. Você verá uma mensagem: **"Workflow is active"**
4. **Copie a URL do webhook** que aparece:
   ```
   https://givaldosj.app.n8n.cloud/webhook/vapi-chamadas
   https://givaldosj.app.n8n.cloud/webhook/whatsapp-mensagens
   https://givaldosj.app.n8n.cloud/webhook/agendar
   https://givaldosj.app.n8n.cloud/webhook/notificar-tecnico
   ```

**Salve essas URLs! Você vai precisar delas!**

---

## 🔗 PASSO 9: CONECTAR WEBHOOKS (Opcional agora)

Você pode fazer isso depois, mas aqui está o resumo:

### No Vapi.ai

1. Acesse: https://dashboard.vapi.ai
2. Vá para **Assistants** → **Alex**
3. Procure por **Webhooks**
4. Adicione:
   - **URL**: (URL do Workflow 1)
   - **Evento**: Call Completed
5. Salve

### No WhatsApp

1. Acesse: https://developers.facebook.com
2. Vá para seu app WhatsApp
3. Configure webhook:
   - **URL**: (URL do Workflow 2)
4. Salve

---

## ✅ CHECKLIST FINAL

- [ ] Arquivo JSON localizado
- [ ] Conteúdo copiado
- [ ] Acessado n8n
- [ ] Workflows importados (4 workflows visíveis)
- [ ] Credenciais do Supabase conectadas (em todos os 4)
- [ ] Todos os 4 workflows testados
- [ ] Todos os 4 workflows ativados
- [ ] URLs dos webhooks copiadas

---

## 🎉 PRONTO!

Seus workflows estão 100% funcionando!

**Próximos passos:**
1. Conectar webhooks no Vapi.ai (opcional agora)
2. Conectar webhooks no WhatsApp (opcional agora)
3. Fazer testes com chamadas reais

---

## 📞 DÚVIDAS?

Se tiver problemas:

1. **Workflows não aparecem após importar?**
   - Atualize a página (F5)
   - Verifique se o JSON foi colado corretamente

2. **Erro ao conectar credenciais?**
   - Crie uma nova credencial do Supabase
   - Use os dados acima

3. **Workflow não ativa?**
   - Verifique se todas as credenciais estão conectadas
   - Clique em "Test" primeiro para verificar erros

4. **Mais ajuda?**
   - Consulte: docs/IMPORTAR_WORKFLOWS_N8N.md
   - Consulte: docs/GUIA_RAPIDO_N8N.md

---

**Você consegue! 💪 Tempo total: ~10 minutos! ⏱️**
