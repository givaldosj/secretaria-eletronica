# 🤖 Secretária Eletrônica - Sistema de Atendimento Automático

[![GitHub](https://img.shields.io/badge/GitHub-givaldosj-blue?style=flat-square&logo=github)](https://github.com/givaldosj)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=flat-square)]()

Sistema completo de secretária eletrônica para atendimento ao cliente 24/7 via voz (Vapi.ai + Twilio) e WhatsApp, com banco de dados, agendamentos automáticos e integração com n8n.

---

## 📋 Sumário

- [Visão Geral](#visão-geral)
- [Recursos](#recursos)
- [Arquitetura](#arquitetura)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Documentação](#documentação)
- [Suporte](#suporte)

---

## 🎯 Visão Geral

Este projeto implementa uma solução completa de secretária eletrônica que permite:

- **Atendimento por Voz**: Assistente IA (Vapi.ai) responde chamadas 24/7
- **Atendimento por WhatsApp**: Respostas automáticas e reconhecimento de mídia
- **Agendamentos**: Sistema automático de agendamentos com verificação de disponibilidade
- **Banco de Dados**: Registro completo de todas as interações
- **Notificações**: Alertas ao técnico sobre chamadas e agendamentos

---

## ✨ Recursos

### 🎤 Atendimento por Voz
- Assistente IA inteligente (Vapi.ai)
- Integração com Twilio para chamadas
- Transcrição automática de conversas
- Resumo inteligente de chamadas
- Agendamento de atendimentos por voz

### 💬 Atendimento por WhatsApp
- Respostas automáticas baseadas em IA
- Reconhecimento de imagens e vídeos
- Armazenamento de histórico
- Agendamento via WhatsApp
- Notificações automáticas

### 📅 Sistema de Agendamentos
- Verificação automática de disponibilidade
- Suporte a múltiplos locais e horários
- Confirmação automática
- Lembretes 24h antes
- Integração com calendário

### 💾 Banco de Dados
- Supabase PostgreSQL
- Tabelas: clientes, chamadas, agendamentos, mensagens_whatsapp, configuracoes
- Índices para performance otimizada
- Backup automático

### 🔄 Automação
- n8n para orquestração de workflows
- Webhooks para integração em tempo real
- Processamento automático de dados
- Notificações inteligentes

---

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────────────────────┐
│                    CLIENTE                                   │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐                    ┌──────────────────┐   │
│  │   Ligação    │                    │   WhatsApp       │   │
│  │   (Vapi.ai)  │                    │   (Mensagens)    │   │
│  └──────┬───────┘                    └────────┬─────────┘   │
│         │                                     │              │
└─────────┼─────────────────────────────────────┼──────────────┘
          │                                     │
          ▼                                     ▼
┌──────────────────────┐          ┌──────────────────────┐
│   Vapi.ai Webhook    │          │  WhatsApp Webhook    │
│   (Chamadas)         │          │  (Mensagens)         │
└──────────┬───────────┘          └──────────┬───────────┘
           │                                 │
           └─────────────────┬───────────────┘
                             │
                             ▼
                    ┌────────────────┐
                    │   n8n Cloud    │
                    │  (Workflows)   │
                    └────────┬───────┘
                             │
                    ┌────────▼────────┐
                    │   Supabase      │
                    │  (PostgreSQL)   │
                    └─────────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
    ┌────────┐          ┌─────────┐          ┌──────────┐
    │Clientes│          │Chamadas │          │Agendamentos
    └────────┘          └─────────┘          └──────────┘
```

---

## 🚀 Instalação

### Pré-requisitos

- Conta no Vapi.ai
- Conta no Twilio
- Conta no Supabase
- Conta no n8n.cloud
- Conta no WhatsApp Business
- Git instalado

### Passo 1: Clonar Repositório

```bash
git clone https://github.com/givaldosj/secretaria-eletronica.git
cd secretaria-eletronica
```

### Passo 2: Configurar Banco de Dados

1. Acesse [Supabase Dashboard](https://supabase.com/dashboard)
2. Crie novo projeto: `SecretariaEletronica`
3. Vá para SQL Editor
4. Cole o conteúdo de `database_schema.sql`
5. Execute o SQL

### Passo 3: Obter Credenciais

Copie as credenciais do Supabase:
- Project URL
- Anon Key
- Service Role Key

### Passo 4: Configurar n8n

Siga o guia em `CONFIGURAR_N8N.md` para criar os workflows.

---

## ⚙️ Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` (não será versionado):

```env
# Supabase
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_ANON_KEY=seu_anon_key
SUPABASE_SERVICE_ROLE_KEY=seu_service_role_key

# Vapi.ai
VAPI_API_KEY=sua_chave_vapi

# WhatsApp
WHATSAPP_TOKEN=seu_token
WHATSAPP_PHONE_ID=seu_phone_id

# Twilio
TWILIO_ACCOUNT_SID=seu_sid
TWILIO_AUTH_TOKEN=seu_token

# n8n
N8N_API_KEY=sua_chave_n8n
```

### Estrutura de Diretórios

```
secretaria-eletronica/
├── README.md                          # Este arquivo
├── .gitignore                         # Arquivo de exclusão
├── LICENSE                            # Licença MIT
│
├── docs/                              # Documentação
│   ├── DOCUMENTACAO_FINAL.md          # Documentação completa
│   ├── CONFIGURAR_N8N.md              # Guia de configuração n8n
│   ├── N8N_WORKFLOWS.md               # Detalhes dos workflows
│   ├── GUIA_SETUP_SUPABASE.md         # Setup do Supabase
│   └── RESUMO_PROJETO.md              # Resumo executivo
│
├── database/                          # Banco de dados
│   └── database_schema.sql            # Schema PostgreSQL
│
├── config/                            # Configurações
│   ├── supabase_credentials.json.example
│   └── n8n_config.json.example
│
├── workflows/                         # Workflows n8n (JSON)
│   ├── vapi-chamadas.json
│   ├── whatsapp-mensagens.json
│   ├── agendamentos.json
│   └── notificacoes.json
│
├── scripts/                           # Scripts auxiliares
│   ├── setup.py
│   ├── test_connection.py
│   └── backup_database.py
│
└── prompts/                           # Prompts da IA
    └── vapi_assistant_alex.txt        # Prompt do Vapi.ai
```

---

## 📖 Documentação

### Documentos Principais

| Documento | Descrição |
|-----------|-----------|
| [DOCUMENTACAO_FINAL.md](docs/DOCUMENTACAO_FINAL.md) | Documentação completa do projeto |
| [CONFIGURAR_N8N.md](docs/CONFIGURAR_N8N.md) | Guia passo a passo para n8n |
| [N8N_WORKFLOWS.md](docs/N8N_WORKFLOWS.md) | Detalhes técnicos dos workflows |
| [GUIA_SETUP_SUPABASE.md](docs/GUIA_SETUP_SUPABASE.md) | Setup do banco de dados |
| [database_schema.sql](database/database_schema.sql) | Schema PostgreSQL |

---

## 🧪 Uso

### Teste 1: Chamada de Voz

```bash
1. Disque para o número configurado no Twilio
2. O assistente Alex responderá
3. Converse naturalmente
4. Verifique em Supabase → chamadas
```

### Teste 2: Mensagem WhatsApp

```bash
1. Envie uma mensagem no WhatsApp
2. Receberá resposta automática
3. Verifique em Supabase → mensagens_whatsapp
```

### Teste 3: Agendamento

```bash
1. Solicite agendamento por voz ou WhatsApp
2. Siga o fluxo de agendamento
3. Verifique em Supabase → agendamentos
```

---

## 📊 Banco de Dados

### Tabelas Principais

#### clientes
Armazena informações dos clientes.

```sql
SELECT * FROM clientes;
```

#### chamadas
Registro de todas as chamadas.

```sql
SELECT * FROM chamadas WHERE criado_em >= NOW() - INTERVAL '7 days';
```

#### agendamentos
Agendamentos de atendimento.

```sql
SELECT * FROM agendamentos WHERE status = 'agendado';
```

#### mensagens_whatsapp
Histórico de mensagens do WhatsApp.

```sql
SELECT * FROM mensagens_whatsapp WHERE direcao = 'entrada';
```

---

## 🔒 Segurança

### Boas Práticas

- ✅ Nunca commitar credenciais
- ✅ Usar `.env` para variáveis sensíveis
- ✅ Validar entrada de dados
- ✅ Usar HTTPS para webhooks
- ✅ Monitorar logs regularmente
- ✅ Fazer backup de dados

### Proteção de Credenciais

As credenciais estão em `.gitignore` e não serão versionadas:

```
supabase_credentials.json
.env
.env.local
```

---

## 🐛 Troubleshooting

### Erro: "Webhook not receiving data"
- Verifique se o webhook está ativo
- Verifique se a URL está correta
- Teste enviando dados manualmente

### Erro: "Supabase connection failed"
- Verifique credenciais
- Teste a conexão manualmente
- Verifique permissões de acesso

### Erro: "Table not found"
- Verifique se executou o SQL
- Verifique nome da tabela
- Verifique permissões

---

## 📞 Suporte

Para suporte:

1. Consulte a documentação em `docs/`
2. Verifique logs de erro em n8n
3. Teste conexões manualmente
4. Entre em contato com o desenvolvedor

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 👤 Autor

**Givaldo**
- GitHub: [@givaldosj](https://github.com/givaldosj)
- Email: givaldosj@gmail.com

---

## 🎯 Roadmap

- [ ] Integração com CRM
- [ ] Dashboard de analytics
- [ ] Relatórios avançados
- [ ] Integração com Google Calendar
- [ ] Suporte a múltiplos idiomas
- [ ] Integração com Slack
- [ ] API REST pública

---

## 📝 Changelog

### v1.0 (Janeiro 2026)
- ✅ Assistente Alex (Vapi.ai)
- ✅ Banco de dados (Supabase)
- ✅ Workflows (n8n)
- ✅ Integração WhatsApp
- ✅ Sistema de agendamentos
- ✅ Documentação completa

---

## 🙏 Agradecimentos

- Vapi.ai por fornecer a plataforma de IA
- Supabase por fornecer o banco de dados
- n8n por fornecer a automação
- Twilio por fornecer as chamadas

---

**Última atualização**: Janeiro 2026
**Status**: ✅ Pronto para Produção
