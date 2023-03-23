sudo systemctl restart file-server
sudo nginx -t && sudo certbot --nginx && sudo systemctl restart nginx 
