#!/usr/bin/env python3
"""
Script para criar as tabelas necessárias no Supabase para a secretária eletrônica
"""

import os
import sys

# Credenciais do Supabase (serão preenchidas manualmente)
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-anon-key"

# SQL para criar as tabelas
CREATE_TABLES_SQL = """
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
    status VARCHAR(50), -- 'completada', 'perdida', 'transferida'
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Agendamentos
CREATE TABLE IF NOT EXISTS agendamentos (
    id BIGSERIAL PRIMARY KEY,
    cliente_id BIGINT REFERENCES clientes(id) ON DELETE CASCADE,
    data_agendamento DATE NOT NULL,
    hora_agendamento TIME NOT NULL,
    local VARCHAR(255), -- 'Rua Rio Grande do Norte' ou 'Rua Maruim'
    servico VARCHAR(255), -- tipo de serviço solicitado
    status VARCHAR(50), -- 'agendado', 'confirmado', 'realizado', 'cancelado'
    notas TEXT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Mensagens WhatsApp
CREATE TABLE IF NOT EXISTS mensagens_whatsapp (
    id BIGSERIAL PRIMARY KEY,
    cliente_id BIGINT REFERENCES clientes(id) ON DELETE CASCADE,
    conteudo TEXT NOT NULL,
    tipo VARCHAR(50), -- 'texto', 'imagem', 'video', 'audio'
    url_midia VARCHAR(500),
    direcao VARCHAR(20), -- 'entrada' ou 'saida'
    status VARCHAR(50), -- 'enviada', 'entregue', 'lida'
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

-- Habilitar RLS (Row Level Security) para segurança
ALTER TABLE clientes ENABLE ROW LEVEL SECURITY;
ALTER TABLE chamadas ENABLE ROW LEVEL SECURITY;
ALTER TABLE agendamentos ENABLE ROW LEVEL SECURITY;
ALTER TABLE mensagens_whatsapp ENABLE ROW LEVEL SECURITY;
ALTER TABLE configuracoes ENABLE ROW LEVEL SECURITY;
"""

print("Script de configuração do Supabase criado!")
print("\nPróximos passos:")
print("1. Acesse o Supabase Dashboard")
print("2. Vá para SQL Editor")
print("3. Cole o SQL acima e execute")
print("\nOu use a API do Supabase para executar automaticamente")
