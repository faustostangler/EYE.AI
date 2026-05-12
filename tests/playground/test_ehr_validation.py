import pytest
import json
from playground.app import ElectronicHealthRecord

def test_ehr_validation_with_dictionary_sintomas():
    """Verify that symptoms as a dictionary are serialized to a string list."""
    data = {
        "queixa_principal": "Visão dupla",
        "historia_doenca_atual": "Início há 2 dias",
        "sintomas": {"strabismus": True, "causes": ["dor de cabeça", "Visão dupla"]},
        "exames_solicitados": ["Tomografia"],
        "diagnostico_hipotese": "Estrabismo",
        "conduta_tratamento": "Encaminhamento",
        "especialidade": "strabismus"
    }
    
    ehr = ElectronicHealthRecord(**data)
    # The validator cast_to_list for sintomas should turn the dict into a JSON string list item
    assert len(ehr.sintomas) == 1
    assert "strabismus" in ehr.sintomas[0]
    assert "causes" in ehr.sintomas[0]

def test_ehr_validation_with_list_in_string_field():
    """Verify that a list provided to a string field is joined."""
    data = {
        "queixa_principal": ["Dor", "e", "Vermelhidão"],
        "historia_doenca_atual": "Início há 2 dias",
        "sintomas": ["Dor"],
        "exames_solicitados": ["Tomografia"],
        "diagnostico_hipotese": "Estrabismo",
        "conduta_tratamento": "Encaminhamento",
        "especialidade": "strabismus"
    }
    
    ehr = ElectronicHealthRecord(**data)
    assert ehr.queixa_principal == "Dor e Vermelhidão"

def test_ehr_validation_with_complex_dict_in_string_field():
    """Verify that a dictionary provided to a string field is serialized to JSON."""
    data = {
        "queixa_principal": "Visão dupla",
        "historia_doenca_atual": "Início há 2 dias",
        "sintomas": ["Dor"],
        "exames_solicitados": ["Tomografia"],
        "diagnostico_hipotese": {"principal": "Estrabismo", "secundario": "Cefaleia"},
        "conduta_tratamento": "Encaminhamento",
        "especialidade": "strabismus"
    }
    
    ehr = ElectronicHealthRecord(**data)
    assert isinstance(ehr.diagnostico_hipotese, str)
    decoded = json.loads(ehr.diagnostico_hipotese)
    assert decoded["principal"] == "Estrabismo"

def test_ehr_validation_with_list_of_dicts():
    """Verify that a list of dictionaries is handled correctly."""
    data = {
        "queixa_principal": "Visão dupla",
        "historia_doenca_atual": "Início há 2 dias",
        "sintomas": [
            {"nome": "Dor de cabeça", "detalhes": "Região da testa"},
            {"nome": "Visão dupla", "detalhes": "Ao olhar para o lado"}
        ],
        "exames_solicitados": [
            {"nome": "Exame ocular", "motivo": "Avaliar estrabismo"}
        ],
        "diagnostico_hipotese": "Estrabismo",
        "conduta_tratamento": "Encaminhamento",
        "especialidade": "strabismus"
    }
    
    ehr = ElectronicHealthRecord(**data)
    # Each dict should be converted to a string (ideally extracting 'nome' or serializing)
    assert len(ehr.sintomas) == 2
    assert isinstance(ehr.sintomas[0], str)
    assert isinstance(ehr.exames_solicitados[0], str)

