---
name: jonathan
description: Visio-Scribe Jonathan - Skill para transcrição de áudios longos (≥ 1h30) com alta eficiência e robustez. Gera output em formato .srt de forma incremental. Use esta skill quando precisar extrair a transcrição estruturada de uma consulta médica (ou arquivo de áudio longo) para integrar ao Prontuário Institucional Estruturado, identificando fala ou gerando a base para um documento clínico.
compatibility: python3, ffmpeg
---

# Visio-Scribe Jonathan

O Jonathan é a interface responsável por transformar longos arquivos de áudio (como consultas médicas de mais de 1h30) em texto estruturado (formato `.srt`).

Ele possui inteligência para lidar com falhas e hardware:
- Detecta a presença de GPU para usar `faster-whisper`.
- Faz fallback em CPU para o `openai-whisper` processando em chunks para evitar sobrecarga de RAM/Timeout.
- Salva o arquivo `.srt` de forma incremental para não perder progresso em caso de interrupção.

## Como usar o Jonathan

Quando o usuário pedir para transcrever um áudio, utilize o script de transcrição interno do Jonathan:

```bash
python .agents/skills/jonathan/scripts/transcribe.py "caminho/para/audio.mp3"
```

Você também pode fornecer um caminho específico para o `.srt`:
```bash
python .agents/skills/jonathan/scripts/transcribe.py "caminho/para/audio.mp3" "caminho/saida.srt"
```

## O Que Acontece nos Bastidores
- O script fará a instalação de dependências se for o primeiro uso (PyTorch, Whisper/Faster-Whisper, Pydub).
- Garantirá chunking seguro no fallback CPU.
- O `.srt` vai aparecer no disco aos poucos, permitindo o acompanhamento progressivo em tempo real.

**NOTA:** Depois que o `.srt` for gerado, você pode processar seu conteúdo separadamente para extrair informações clínicas e formatar segundo o vocabulário da especialidade (de acordo com as diretrizes do DocTheraBot AI).
