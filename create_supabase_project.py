#!/usr/bin/env python3
"""
Script para criar projeto e tabelas no Supabase usando a API
"""

import requests
import json
import time
import os

# Credenciais
EMAIL = "givaldosj@gmail.com"
PASSWORD = "Thiago2248tA@@"
ORG_ID = "bmmffaoajvsqflfrefhz"  # ID da organização Jr Tech

# URLs
AUTH_URL = "https://api.supabase.io/v1/auth"
API_URL = "https://api.supabase.io/v1"

def login():
    """Fazer login no Supabase"""
    print("🔐 Fazendo login no Supabase...")
    
    response = requests.post(
        f"{AUTH_URL}/sign-in",
        json={
            "email": EMAIL,
            "password": PASSWORD
        }
    )
    
    if response.status_code != 200:
        print(f"❌ Erro ao fazer login: {response.text}")
        return None
    
    data = response.json()
    token = data.get("session", {}).get("access_token")
    print(f"✅ Login realizado com sucesso!")
    return token

def create_project(token):
    """Criar novo projeto no Supabase"""
    print("\n📦 Criando projeto SecretariaEletronica...")
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "name": "SecretariaEletronica",
        "organization_id": ORG_ID,
        "db_pass": "pC3IPSXIW4rcgnXY",
        "region": "sa-east-1",  # São Paulo
        "plan": "free"
    }
    
    response = requests.post(
        f"{API_URL}/projects",
        headers=headers,
        json=payload
    )
    
    if response.status_code not in [200, 201]:
        print(f"❌ Erro ao criar projeto: {response.text}")
        return None
    
    data = response.json()
    project_id = data.get("id")
    print(f"✅ Projeto criado com ID: {project_id}")
    
    # Aguardar projeto ficar pronto
    print("⏳ Aguardando projeto ficar pronto...")
    time.sleep(10)
    
    return project_id

def get_project_details(token, project_id):
    """Obter detalhes do projeto"""
    print(f"\n📋 Obtendo detalhes do projeto...")
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(
        f"{API_URL}/projects/{project_id}",
        headers=headers
    )
    
    if response.status_code != 200:
        print(f"❌ Erro ao obter detalhes: {response.text}")
        return None
    
    data = response.json()
    
    project_url = data.get("project_ref")
    print(f"✅ URL do Projeto: https://{project_url}.supabase.co")
    
    return data

def main():
    """Função principal"""
    print("=" * 60)
    print("🚀 SETUP DO SUPABASE - SECRETÁRIA ELETRÔNICA")
    print("=" * 60)
    
    # Login
    token = login()
    if not token:
        return False
    
    # Criar projeto
    project_id = create_project(token)
    if not project_id:
        return False
    
    # Obter detalhes
    project_data = get_project_details(token, project_id)
    if not project_data:
        return False
    
    print("\n" + "=" * 60)
    print("✅ PROJETO CRIADO COM SUCESSO!")
    print("=" * 60)
    print(f"\nPróximos passos:")
    print("1. Aguarde 2-3 minutos para o projeto ficar completamente pronto")
    print("2. Acesse o Supabase Dashboard")
    print("3. Vá para SQL Editor")
    print("4. Cole o conteúdo de database_schema.sql e execute")
    print("5. Copie as chaves de API em Settings > API")
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
