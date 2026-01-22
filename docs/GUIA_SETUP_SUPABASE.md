# 🚀 GUIA COMPLETO - SETUP SUPABASE

## ⏱️ Tempo estimado: 5 minutos

---

## PASSO 1: Criar o Projeto (2 minutos)

### 1.1 Acesse o Supabase
- Abra este link: https://supabase.com/dashboard/organizations
- Você já estará logado (a sessão está ativa)

### 1.2 Clique em "New project"
- Procure pelo botão verde "New project" ou "+ New project"
- Clique nele

### 1.3 Preencha o formulário
Preencha com exatamente estes dados:

| Campo | Valor |
|-------|-------|
| **Organization** | Jr Tech FREE |
| **Project name** | `SecretariaEletronica` |
| **Database password** | `pC3IPSXIW4rcgnXY` |
| **Region** | South America (São Paulo) - sa-east-1 |

### 1.4 Clique em "Create new project"
- O projeto começará a ser criado
- Aguarde 2-3 minutos para ficar pronto
- Você verá uma tela de carregamento

---

## PASSO 2: Executar o SQL para Criar as Tabelas (2 minutos)

### 2.1 Após o projeto ficar pronto
- Você será redirecionado para o dashboard do projeto
- Procure pelo menu lateral esquerdo

### 2.2 Vá para "SQL Editor"
- No menu lateral, clique em **SQL Editor** (ou **SQL**)
- Você verá um editor de código em branco

### 2.3 Cole o SQL
- Abra o arquivo: `/home/ubuntu/secretaria_eletronica/database_schema.sql`
- Copie **TODO** o conteúdo
- Cole no editor SQL do Supabase

### 2.4 Execute o SQL
- Clique no botão **"Run"** (verde)
- Ou pressione **Ctrl+Enter**
- Aguarde a execução (deve ser rápido)
- Você verá mensagens de sucesso

---

## PASSO 3: Obter as Credenciais (1 minuto)

### 3.1 Vá para "Settings"
- No menu lateral, clique em **Settings**

### 3.2 Vá para "API"
- Procure pela aba **API**
- Clique nela

### 3.3 Copie as 3 chaves necessárias
Você verá 3 chaves importantes:

1. **Project URL** (ex: `https://xxxxxxxxxxxxx.supabase.co`)
   - Copie e guarde

2. **anon public** (chave pública)
   - Copie e guarde

3. **service_role** (chave privada)
   - Copie e guarde

---

## ✅ PRONTO!

Depois que tiver as 3 credenciais acima, me avise com:

```
Project URL: https://xxxxx.supabase.co
Anon Key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Service Role Key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Então vou:
1. ✅ Configurar o n8n automaticamente
2. ✅ Criar os workflows para Vapi.ai
3. ✅ Integrar com WhatsApp
4. ✅ Configurar agendamentos automáticos
5. ✅ Testar tudo

---

## 📝 OBSERVAÇÕES

- **Não perca as credenciais!** Salve em um lugar seguro
- O projeto leva 2-3 minutos para ficar pronto após clicar em "Create"
- Se algo der errado, você pode deletar o projeto e criar novamente
- Qualquer dúvida, me avise!

---

## 🔗 LINKS RÁPIDOS

- Supabase Dashboard: https://supabase.com/dashboard/organizations
- Seu Projeto: https://supabase.com/dashboard/org/bmmffaoajvsqflfrefhz

---

**Comece agora! Leva apenas 5 minutos! 🚀**
