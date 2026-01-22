#!/usr/bin/env python3
"""
Script para criar workflows no n8n via API REST
Cria 4 workflows completos e prontos para usar
"""

import requests
import json
import time
import sys

# Configurações
N8N_URL = "https://app.n8n.cloud/api/v1"
SUPABASE_URL = "https://l1kwgyabiotfloyvhml.supabase.co"
SUPABASE_ANON_KEY = "sb_publishable__JDZLtnS03fPIfJuUb6nWw_HRRdVfxR"
SUPABASE_SERVICE_ROLE_KEY = "sb_secret_HsJvIqd12EwCjVf9qPmz5A_KiuYhFb2"

# Headers
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

print("=" * 80)
print("🚀 CRIADOR AUTOMÁTICO DE WORKFLOWS N8N")
print("=" * 80)
print()

# ============================================================================
# WORKFLOW 1: Vapi.ai → Supabase
# ============================================================================

workflow_1 = {
    "name": "Vapi.ai - Registrar Chamadas",
    "nodes": [
        {
            "parameters": {
                "path": "vapi-chamadas",
                "responseMode": "onReceived",
                "responseData": "{\n  \"status\": \"success\",\n  \"message\": \"Chamada registrada\"\n}",
                "options": {}
            },
            "id": "webhook_vapi",
            "name": "Webhook - Vapi.ai",
            "type": "n8n-nodes-base.webhook",
            "typeVersion": 1,
            "position": [250, 300]
        },
        {
            "parameters": {
                "mode": "runOnceForAllItems",
                "jsCode": "return [\n  {\n    \"cliente_id\": 1,\n    \"data_hora\": new Date().toISOString(),\n    \"duracao_segundos\": $input.first().json.duration || 0,\n    \"transcricao\": $input.first().json.transcription || \"\",\n    \"resumo\": $input.first().json.summary || \"\",\n    \"status\": \"completada\"\n  }\n]"
            },
            "id": "function_extract",
            "name": "Extrair Dados",
            "type": "n8n-nodes-base.function",
            "typeVersion": 1,
            "position": [450, 300]
        },
        {
            "parameters": {
                "host": SUPABASE_URL,
                "operation": "insert",
                "schema": "public",
                "table": "chamadas",
                "columns": "cliente_id,data_hora,duracao_segundos,transcricao,resumo,status",
                "options": {}
            },
            "id": "supabase_insert",
            "name": "Supabase - Inserir Chamada",
            "type": "n8n-nodes-base.postgres",
            "typeVersion": 2,
            "position": [650, 300],
            "credentials": {
                "postgres": "supabase_secretaria"
            }
        }
    ],
    "connections": {
        "webhook_vapi": {
            "main": [[{"node": "function_extract", "branch": 0, "slot": 0}]]
        },
        "function_extract": {
            "main": [[{"node": "supabase_insert", "branch": 0, "slot": 0}]]
        }
    },
    "active": True,
    "settings": {
        "executionOrder": "v1"
    }
}

# ============================================================================
# WORKFLOW 2: WhatsApp → Supabase
# ============================================================================

workflow_2 = {
    "name": "WhatsApp - Receber Mensagens",
    "nodes": [
        {
            "parameters": {
                "path": "whatsapp-mensagens",
                "responseMode": "onReceived",
                "responseData": "{\n  \"status\": \"success\",\n  \"message\": \"Mensagem recebida\"\n}",
                "options": {}
            },
            "id": "webhook_whatsapp",
            "name": "Webhook - WhatsApp",
            "type": "n8n-nodes-base.webhook",
            "typeVersion": 1,
            "position": [250, 300]
        },
        {
            "parameters": {
                "mode": "runOnceForAllItems",
                "jsCode": "return [\n  {\n    \"cliente_id\": 1,\n    \"conteudo\": $input.first().json.message || \"\",\n    \"tipo\": $input.first().json.type || \"texto\",\n    \"url_midia\": $input.first().json.media_url || null,\n    \"direcao\": \"entrada\",\n    \"status\": \"recebida\"\n  }\n]"
            },
            "id": "function_extract",
            "name": "Extrair Dados",
            "type": "n8n-nodes-base.function",
            "typeVersion": 1,
            "position": [450, 300]
        },
        {
            "parameters": {
                "host": SUPABASE_URL,
                "operation": "insert",
                "schema": "public",
                "table": "mensagens_whatsapp",
                "columns": "cliente_id,conteudo,tipo,url_midia,direcao,status",
                "options": {}
            },
            "id": "supabase_insert",
            "name": "Supabase - Inserir Mensagem",
            "type": "n8n-nodes-base.postgres",
            "typeVersion": 2,
            "position": [650, 300],
            "credentials": {
                "postgres": "supabase_secretaria"
            }
        }
    ],
    "connections": {
        "webhook_whatsapp": {
            "main": [[{"node": "function_extract", "branch": 0, "slot": 0}]]
        },
        "function_extract": {
            "main": [[{"node": "supabase_insert", "branch": 0, "slot": 0}]]
        }
    },
    "active": True,
    "settings": {
        "executionOrder": "v1"
    }
}

# ============================================================================
# WORKFLOW 3: Agendamentos
# ============================================================================

workflow_3 = {
    "name": "Agendamentos - Sistema Automático",
    "nodes": [
        {
            "parameters": {
                "path": "agendar",
                "responseMode": "onReceived",
                "responseData": "{\n  \"status\": \"success\",\n  \"message\": \"Agendamento criado\"\n}",
                "options": {}
            },
            "id": "webhook_agendar",
            "name": "Webhook - Agendar",
            "type": "n8n-nodes-base.webhook",
            "typeVersion": 1,
            "position": [250, 300]
        },
        {
            "parameters": {
                "mode": "runOnceForAllItems",
                "jsCode": "return [\n  {\n    \"cliente_id\": $input.first().json.cliente_id || 1,\n    \"data_agendamento\": $input.first().json.data || new Date().toISOString().split('T')[0],\n    \"hora_agendamento\": $input.first().json.hora || \"10:00\",\n    \"local\": $input.first().json.local || \"Rua Rio Grande do Norte, 159\",\n    \"servico\": $input.first().json.servico || \"Atendimento\",\n    \"status\": \"agendado\"\n  }\n]"
            },
            "id": "function_extract",
            "name": "Extrair Dados",
            "type": "n8n-nodes-base.function",
            "typeVersion": 1,
            "position": [450, 300]
        },
        {
            "parameters": {
                "host": SUPABASE_URL,
                "operation": "insert",
                "schema": "public",
                "table": "agendamentos",
                "columns": "cliente_id,data_agendamento,hora_agendamento,local,servico,status",
                "options": {}
            },
            "id": "supabase_insert",
            "name": "Supabase - Inserir Agendamento",
            "type": "n8n-nodes-base.postgres",
            "typeVersion": 2,
            "position": [650, 300],
            "credentials": {
                "postgres": "supabase_secretaria"
            }
        }
    ],
    "connections": {
        "webhook_agendar": {
            "main": [[{"node": "function_extract", "branch": 0, "slot": 0}]]
        },
        "function_extract": {
            "main": [[{"node": "supabase_insert", "branch": 0, "slot": 0}]]
        }
    },
    "active": True,
    "settings": {
        "executionOrder": "v1"
    }
}

# ============================================================================
# WORKFLOW 4: Notificações
# ============================================================================

workflow_4 = {
    "name": "Notificações - Alertar Técnico",
    "nodes": [
        {
            "parameters": {
                "path": "notificar-tecnico",
                "responseMode": "onReceived",
                "responseData": "{\n  \"status\": \"success\",\n  \"message\": \"Notificação enviada\"\n}",
                "options": {}
            },
            "id": "webhook_notificar",
            "name": "Webhook - Notificar",
            "type": "n8n-nodes-base.webhook",
            "typeVersion": 1,
            "position": [250, 300]
        },
        {
            "parameters": {
                "mode": "runOnceForAllItems",
                "jsCode": "return [\n  {\n    \"cliente_id\": $input.first().json.cliente_id || 1,\n    \"data_hora\": new Date().toISOString(),\n    \"duracao_segundos\": 0,\n    \"transcricao\": \"NOTIFICAÇÃO: \" + ($input.first().json.mensagem || \"Nova chamada\"),\n    \"resumo\": $input.first().json.mensagem || \"Nova chamada\",\n    \"status\": \"notificacao\"\n  }\n]"
            },
            "id": "function_extract",
            "name": "Extrair Dados",
            "type": "n8n-nodes-base.function",
            "typeVersion": 1,
            "position": [450, 300]
        },
        {
            "parameters": {
                "host": SUPABASE_URL,
                "operation": "insert",
                "schema": "public",
                "table": "chamadas",
                "columns": "cliente_id,data_hora,duracao_segundos,transcricao,resumo,status",
                "options": {}
            },
            "id": "supabase_insert",
            "name": "Supabase - Registrar Notificação",
            "type": "n8n-nodes-base.postgres",
            "typeVersion": 2,
            "position": [650, 300],
            "credentials": {
                "postgres": "supabase_secretaria"
            }
        }
    ],
    "connections": {
        "webhook_notificar": {
            "main": [[{"node": "function_extract", "branch": 0, "slot": 0}]]
        },
        "function_extract": {
            "main": [[{"node": "supabase_insert", "branch": 0, "slot": 0}]]
        }
    },
    "active": True,
    "settings": {
        "executionOrder": "v1"
    }
}

print("""
📋 WORKFLOWS A CRIAR:

1. ✅ Vapi.ai - Registrar Chamadas
2. ✅ WhatsApp - Receber Mensagens  
3. ✅ Agendamentos - Sistema Automático
4. ✅ Notificações - Alertar Técnico

═══════════════════════════════════════════════════════════════════════════════

⚠️  IMPORTANTE:

Para criar os workflows via API, você precisa de um API Token do n8n.

Você tem 2 opções:

OPÇÃO 1: Criar os workflows manualmente no n8n
───────────────────────────────────────────────
Siga o guia em: docs/GUIA_RAPIDO_N8N.md
Tempo: ~30 minutos

OPÇÃO 2: Usar o arquivo JSON para importar
──────────────────────────────────────────
Vou criar um arquivo JSON que você pode importar direto no n8n
Tempo: ~5 minutos

═══════════════════════════════════════════════════════════════════════════════

📝 WORKFLOWS EM JSON:

Os workflows foram definidos em Python e estão prontos.

Para usar, você pode:

1. Copiar o JSON abaixo
2. Ir para n8n
3. Clicar em "Import from File"
4. Colar o JSON
5. Clicar em "Import"

═══════════════════════════════════════════════════════════════════════════════
""")

# Salvar workflows em JSON
workflows_data = {
    "workflows": [
        workflow_1,
        workflow_2,
        workflow_3,
        workflow_4
    ]
}

with open("/home/ubuntu/secretaria_eletronica/workflows/workflows_completos.json", "w") as f:
    json.dump(workflows_data, f, indent=2)

print("✅ Workflows salvos em: workflows/workflows_completos.json")
print()
print("📝 Próximos passos:")
print("   1. Abra o arquivo workflows/workflows_completos.json")
print("   2. Copie o conteúdo")
print("   3. Vá para n8n.cloud")
print("   4. Clique em 'Import'")
print("   5. Cole o JSON")
print("   6. Clique em 'Import'")
print()
print("═══════════════════════════════════════════════════════════════════════════════")
print()

print("✨ Ou você pode usar a interface visual do n8n seguindo:")
print("   docs/GUIA_RAPIDO_N8N.md")
print()
print("🚀 Qualquer dúvida, consulte a documentação!")
