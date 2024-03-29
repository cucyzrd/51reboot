server {{
    listen       {PORT} default_server;
    server_name  {SERVER_NAME};

    access_log  {ACCESS_LOG}  main;

    location / {{
        root   {ROOT};
        index  index.html index.htm;
        proxy_pass   {PROXY_PASS};
    }}
}}