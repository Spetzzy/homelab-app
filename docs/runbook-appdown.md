# Runbook: AppDown

**Meaning:** Prometheus cannot scrape homelab-app for 30 seconds or more.

## Check, in order
1. Is the container running? `docker compose ps`
2. Why did it stop? `docker compose logs --tail 50 app`
3. Is the port reachable? `curl http://localhost:8080/health`
4. Did a deployment just happen? Check the version in the health response.

## Fix
- Stopped: `docker compose start app`
- Bad release: roll back with `APP_VERSION=<previous> docker compose up -d --no-build`
- Database unhealthy: `docker compose logs db`

## After
Record what happened and what prevents it in docs/troubleshooting.md.
