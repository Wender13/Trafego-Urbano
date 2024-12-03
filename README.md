# 🚦 Sistema de Análise de Tráfego Urbano

## 📝 Descrição do Projeto
O **Sistema de Análise de Tráfego Urbano** é uma ferramenta desenvolvida para monitorar, analisar e visualizar o fluxo de tráfego em diferentes regiões urbanas.  
Utiliza técnicas avançadas de **estruturas de dados**, como tabelas hash, para armazenar informações de veículos de forma eficiente, permitindo consultas rápidas e precisas.

📊 **Objetivo principal:**  
- Identificar padrões de tráfego  
- Localizar áreas congestionadas  
- Fornecer insights para o planejamento urbano  

---

## ⚙️ Funcionalidades
- 🚗 **Cadastro de Veículos:** Registre dados como placa, modelo e localização.  
- 🔍 **Consulta Rápida:** Busque informações de veículos de forma eficiente.  
- 📈 **Análise de Tráfego:** Geração de rankings de congestionamento por região.  
- 🗺️ **Visualização Interativa:** Criação de mapas dinâmicos com zonas críticas de tráfego.  
- 🧪 **Simulação de Tráfego:** Realize testes com grandes volumes de dados.  

---

## 💾 Estrutura de Dados
A implementação utiliza tabelas hash para otimizar armazenamento e manipulação de informações.  

### Métodos principais:
- `inserir(placa, modelo, localizacao)`  
  Adiciona um veículo à tabela hash.  
- `buscar(placa)`  
  Retorna informações sobre um veículo específico.  
- `excluir(placa)`  
  Remove um veículo do sistema.  
- `contar_veiculos(setor)`  
  Conta veículos em uma região específica.  

---

## 🚀 Simulações
Foram realizados testes com até **100.000 registros** para validar:  
- **Inserção** ✅  
- **Busca** ✅  
- **Listagem** ✅  

⏱️ Os resultados mostraram alta eficiência e escalabilidade em todos os cenários.

---

## 🌍 Visualização Geográfica
Utilizando as bibliotecas **GeoPandas** e **Matplotlib**, o sistema gera mapas interativos com dados reais do IBGE.  
🎯 Região analisada: **Município de Goiânia**  
Os mapas destacam zonas de alto tráfego, facilitando análises visuais.  

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 🐍  
- **Bibliotecas:** GeoPandas, Matplotlib, Random, Pandas, CSV  
- **Ambiente de Teste:** Google Colab ☁️ 
