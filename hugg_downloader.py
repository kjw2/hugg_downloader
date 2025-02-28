#!/usr/bin/env python3
import os
import click
from huggingface_hub import hf_hub_download, snapshot_download
from tqdm import tqdm

@click.group()
def cli():
    """허깅페이스 모델/데이터셋 다운로더"""
    pass

def ensure_dir(path):
    """디렉토리가 없으면 생성합니다."""
    if not os.path.exists(path):
        os.makedirs(path)

@cli.command()
@click.argument('repo_id')
@click.option('--filename', '-f', help='다운로드할 특정 파일명')
@click.option('--output-dir', '-o', default='downloads', help='다운로드 기본 저장 경로')
@click.option('--revision', '-r', default='main', help='리비전/브랜치명')
def download(repo_id, filename, output_dir, revision):
    """허깅페이스 모델 또는 데이터셋을 다운로드합니다."""
    try:
        # 기본 다운로드 폴더 생성
        ensure_dir(output_dir)
        
        # 모델명으로 하위 폴더 경로 생성
        model_dir = os.path.join(output_dir, repo_id.split('/')[-1])
        ensure_dir(model_dir)
        
        if filename:
            # 단일 파일 다운로드
            print(f"'{filename}' 파일을 다운로드 중...")
            file_path = hf_hub_download(
                repo_id=repo_id,
                filename=filename,
                revision=revision,
                local_dir=model_dir
            )
            print(f"다운로드 완료: {file_path}")
        else:
            # 전체 저장소 다운로드
            print(f"저장소 '{repo_id}' 전체를 다운로드 중...")
            local_dir = snapshot_download(
                repo_id=repo_id,
                revision=revision,
                local_dir=model_dir
            )
            print(f"다운로드 완료: {local_dir}")
            
    except Exception as e:
        print(f"오류 발생: {str(e)}")

if __name__ == '__main__':
    cli() 