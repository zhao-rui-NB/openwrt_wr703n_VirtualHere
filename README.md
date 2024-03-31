# openwrt_wr703n_VirtualHere

# openwrt wr703n VirtualHere
## 固件
`lede-17.01.7-ar71xx-generic-tl-wr703n-v1-squashfs-factory.bin` 3840KB
## VirtualHere
`vhusbdmips` , 421KB
# openwrt 設置




## Network > interfaces 
lan > edit >
ipv4 adderss 192.168.5.1

## Network > wireless
remove all
### LAN AP
Add Master
```
ESSID OpenWrt_wr703n
firewall-zone wan
mode:access point
wireless securlity:WPA2-PSK
key: 00000000

``` 
### WAN Client
Scan WIFI
connect to wifi

## Network > firewall
取消勾選 SYN-flood protection
all set to accept
wan 的 querading 一定要勾


# 4M 儲存空間
```
root@LEDE:~# df
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/root                 2304      2304         0 100% /rom
tmpfs                    14056       580     13476   4% /tmp
/dev/mtdblock3             384       240       144  63% /overlay
overlayfs:/overlay         384       240       144  63% /
tmpfs                      512         0       512   0% /dev
```
只有/tmp 空間夠大 但斷電丟失

# 上傳執行
每次重啟皆須重新運行
```
auto_run.bat
```