# tendermint_application

1) docker-compose down
2) sudo rm -r hayoola
3) mkdir hayoola
4) chmod 777 hayoola
5) docker-compose run tendermint init
6) sudo nano hayoola/config/config.toml
  proxy_app = tcp://kvstore-app:26658
  pex = false
  create_empty_blocks = false
  [p2p]
  laddr = tcp://0.0.0.0:26656
  [rpc]
  laddr = tcp://0.0.0.0:26657
  prometheus = true  
7) docker-compose up -d
8) (venv) python inotify_tendermint.py
9) (venv) python get_ring_file.py
