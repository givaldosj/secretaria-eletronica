#!/usr/bin/env python3
"""
Script completo para setup do Supabase - Secretária Eletrônica
Cria o projeto e as tabelas necessárias
"""

import requests
import json
import time
from datetime import datetime

# Configurações
SUPABASE_ORG_ID = "bmmffaoajvsqflfrefhz"
PROJECT_NAME = "SecretariaEletronica"
DB_PASSWORD = "pC3IPSXIW4rcgnXY"
REGION = "sa-east-1"  # São Paulo

print("=" * 70)
print("🚀 CONFIGURAÇÃO COMPLETA - SECRETÁRIA ELETRÔNICA")
print("=" * 70)

# Informações que você precisa fornecer manualmente
print("\n📋 INSTRUÇÕES PARA CRIAR O PROJETO MANUALMENTE:\n")

print("1️⃣  CRIAR PROJETO NO SUPABASE:")
print("   - Acesse: https://supabase.com/dashboard/org/" + SUPABASE_ORG_ID)
print("   - Clique em 'New project'")
print("   - Preencha com:")
print(f"     • Project name: {PROJECT_NAME}")
print(f"     • Database password: {DB_PASSWORD}")
print(f"     • Region: South America (São Paulo) - sa-east-1")
print("   - Clique em 'Create new project'")
print("   - Aguarde 2-3 minutos para o projeto ficar pronto\n")

print("2️⃣  CRIAR AS TABELAS:")
print("   - Acesse o projeto criado")
print("   - Vá para 'SQL Editor'")
print("   - Cole todo o conteúdo do arquivo: database_schema.sql")
print("   - Clique em 'Run' ou pressione Ctrl+Enter\n")

print("3️⃣  OBTER AS CREDENCIAIS:")
print("   - Vá para 'Settings' > 'API'")
print("   - Copie e guarde:")
print("     • Project URL (ex: https://xxxxx.supabase.co)")
print("     • anon public key")
print("     • service_role key\n")

print("=" * 70)
print("📝 ARQUIVO SQL PARA COPIAR E COLAR:")
print("=" * 70)

# SQL completo
sql_schema = """
-- ============================================
-- SCHEMA DO BANCO DE DADOS - SECRETÁRIA ELETRÔNICA
-- ============================================

-- Tabela de Clientes
CREATE TABLE IF NOT EXISTS clientes (
    id BIGSERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20) NOT NULL UNIQUE,
    veiculo_modelo VARCHAR(255),
    veiculo_ano INTEGER,
    veiculo_motor VARCHAR(255),
    veiculo_placa VARCHAR(20),
    historico TEXT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Chamadas
CREATE TABLE IF NOT EXISTS chamadas (
    id BIGSERIAL PRIMARY KEY,
    cliente_id BIGINT REFERENCES clientes(id) ON DELETE CASCADE,
    data_hora TIMESTAMP NOT NULL,
    duracao_segundos INTEGER,
    transcricao TEXT,
    resumo TEXT,
    status VARCHAR(50),
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Agendamentos
CREATE TABLE IF NOT EXISTS agendamentos (
    id BIGSERIAL PRIMARY KEY,
    cliente_id BIGINT REFERENCES clientes(id) ON DELETE CASCADE,
    data_agendamento DATE NOT NULL,
    hora_agendamento TIME NOT NULL,
    local VARCHAR(255),
    servico VARCHAR(255),
    status VARCHAR(50),
    notas TEXT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Mensagens WhatsApp
CREATE TABLE IF NOT EXISTS mensagens_whatsapp (
    id BIGSERIAL PRIMARY KEY,
    cliente_id BIGINT REFERENCES clientes(id) ON DELETE CASCADE,
    conteudo TEXT NOT NULL,
    tipo VARCHAR(50),
    url_midia VARCHAR(500),
    direcao VARCHAR(20),
    status VARCHAR(50),
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Configurações
CREATE TABLE IF NOT EXISTS configuracoes (
    id BIGSERIAL PRIMARY KEY,
    chave VARCHAR(255) NOT NULL UNIQUE,
    valor TEXT NOT NULL,
    descricao TEXT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criar índices para melhor performance
CREATE INDEX IF NOT EXISTS idx_chamadas_cliente_id ON chamadas(cliente_id);
CREATE INDEX IF NOT EXISTS idx_chamadas_data_hora ON chamadas(data_hora);
CREATE INDEX IF NOT EXISTS idx_agendamentos_cliente_id ON agendamentos(cliente_id);
CREATE INDEX IF NOT EXISTS idx_agendamentos_data ON agendamentos(data_agendamento);
CREATE INDEX IF NOT EXISTS idx_mensagens_cliente_id ON mensagens_whatsapp(cliente_id);
CREATE INDEX IF NOT EXISTS idx_mensagens_criado_em ON mensagens_whatsapp(criado_em);

-- Inserir configurações iniciais
INSERT INTO configuracoes (chave, valor, descricao) VALUES
('local_1_endereco', 'Rua Rio Grande do Norte, 159, Bairro Dezoito do Forte, Aracaju-Sergipe', 'Endereço do Local A - Recebimento de módulos'),
('local_1_horario_manha_inicio', '08:00', 'Horário de abertura manhã - Local A'),
('local_1_horario_manha_fim', '12:00', 'Horário de fechamento manhã - Local A'),
('local_1_horario_tarde_inicio', '14:00', 'Horário de abertura tarde - Local A'),
('local_1_horario_tarde_fim', '18:00', 'Horário de fechamento tarde - Local A'),
('local_2_endereco', 'Rua Maruim, 1122, Bairro Cirurgia, Aracaju-Sergipe', 'Endereço do Local B - Atendimento com técnico'),
('local_2_horario_manha_inicio', '08:30', 'Horário de abertura manhã - Local B'),
('local_2_horario_manha_fim', '10:00', 'Horário de fechamento manhã - Local B'),
('local_2_horario_tarde_inicio', '16:00', 'Horário de abertura tarde - Local B'),
('local_2_horario_tarde_fim', '17:00', 'Horário de fechamento tarde - Local B'),
('empresa_nome', 'JuniorTech', 'Nome da empresa'),
('empresa_descricao', 'Especializada em serviços de bancada para mecatrônica automotiva', 'Descrição da empresa')
ON CONFLICT (chave) DO NOTHING;
"""

print(sql_schema)

print("\n" + "=" * 70)
print("✅ PRÓXIMOS PASSOS APÓS CRIAR O PROJETO:")
print("=" * 70)
print("""
1. Após obter as credenciais do Supabase, me avise
2. Vou configurar o n8n com essas credenciais
3. Vou criar os workflows para:
   - Integração com Vapi.ai (registrar chamadas)
   - Integração com WhatsApp (receber/enviar mensagens)
   - Sistema de agendamento automático
   - Notificações ao técnico

4. Depois vou testar tudo e entregar a documentação completa
""")

print("=" * 70)
print("📞 INFORMAÇÕES IMPORTANTES:")
print("=" * 70)
print(f"""
• Email: givaldosj@gmail.com
• Organização: Jr Tech
• Projeto: {PROJECT_NAME}
• Região: South America (São Paulo) - {REGION}
• Senha do BD: {DB_PASSWORD}

Todos os arquivos estão em: /home/ubuntu/secretaria_eletronica/
""")
