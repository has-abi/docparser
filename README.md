# DOCPARSER 0.1.0

### For Ubuntu LTS 22.04
You may get the error 'No useable version of libssl' it's due to a change in the libssl version.

**Fix bellow**

```bash
wget "http://security.ubuntu.com/ubuntu/pool/main/o/openssl1.0/libssl1.0.0_1.0.2n-1ubuntu5.10_amd64.deb"
sudo dpkg -i libssl1.0.0_1.0.2n-1ubuntu5.10_amd64.deb
```
