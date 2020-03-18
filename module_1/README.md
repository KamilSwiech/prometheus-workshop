# 0.1 Prerequsites

# Module 1

1.  Docker on local machine
2.  Kind cluster
3.  Internet connection on local machine

#### Kind instalation

##### With Linux

```
curl -Lo ./kind https://github.com/kubernetes-sigs/kind/releases/download/v0.7.0/kind-$(uname)-amd64
chmod +x ./kind
mv ./kind /usr/local/sbin/kind #or any other PATH directory
```

##### With GO

Install go package:

1.  Download archive from  https://golang.org/dl/
2.  Extract: `tar -C /usr/local -xzf go$VERSION.$OS-$ARCH.tar.gz`
3.  Add go bin to your PATH env `export PATH=$PATH:/usr/local/go/bin`
4.  Set GOPATH env https://golang.org/cmd/go/#hdr-Environment_variables and add bin subfolder to PATH env
```
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
```
5.  Install kind `GO111MODULE="on" go get sigs.k8s.io/kind@v0.7.0`


#### Kind startup

Use `kind create cluster --conifg kind-config.yaml`
