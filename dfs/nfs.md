# Configuração do NFS no Linux

Configurar o **NFS (Network File System)** no Linux permite compartilhar arquivos entre máquinas na mesma rede. Aqui estão os passos básicos para configurar um servidor e um cliente NFS.

## Pré-requisitos
- Um servidor Linux para compartilhar os arquivos.
- Um cliente Linux que acessará os arquivos compartilhados.
- Conexão de rede entre os dois dispositivos.

## 1. Instalar o NFS

### Servidor 
#### Instale o pacote NFS:
```bash
sudo apt update
sudo apt install nfs-kernel-server
```

#### Crie o Diretório que será compartilhado
```bash
sudo mkdir -p /mnt/nfs_share
```

#### Altere as permissões do diretório. Lembre-se que você pode usar o comando chown e dar apenas permissões de leitura
```bash
sudo chown nobody:nogroup /mnt/nfs_share
```
#### Abra o arquivo para exportar o diretório
```bash
sudo nano /etc/exports
```

#### Verifique o IP da sua máquina para adicionar a faixa de IPs correta
```bash
ip addr show
```

#### Adicione esta linha para exportar o diretório   
```bash
/mnt/nfs_share 192.168.1.0/24(rw,sync,no_subtree_check)
```

#### Exporte o sistema de arquivos e reinicialize o servidor de arquivos 
```bash
sudo exportfs -ra
sudo systemctl restart nfs-kernel-server
```

#### Verifique se o diretório foi exportado corretamente
```bash
mount | grep nfs
```


### Cliente 
#### Instale o NFS Cliente
```bash
sudo apt update
sudo apt install nfs-common
```
#### Crie o ponto de montagem
```bash
sudo mkdir -p /mnt/nfs_client
```
#### Monte o diretório remoto. Altere o IP abaixo para o IP da máquina servidora
```bash
sudo mount 192.168.1.100:/mnt/nfs_share /mnt/nfs_client
```

