#!/bin/bash
ROOT_DIR=$(dirname "$(realpath "$0")")
HOST='0.0.0.0'
PORT=8000
LOGS_DIR="$ROOT_DIR/logs"

YELLOW='\033[1;33m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

run(){
    echo -e "${YELLOW}Starting Api Gateway service...${NC}"
    nohup uvicorn src.main:app --host $HOST --port $PORT > logs/output.log 2>&1 &
    echo -e "${GREEN}Api Gateway service started. Check logs in $LOGS_DIR${NC}"
}

stop(){
    echo -e "${YELLOW}Stopping Api Gateway...${NC}"
    processID=$(pgrep -f "uvicorn src.main:app")
    if [[ -n "$processID" ]]; then
        kill $processID
        echo -e "${GREEN}Api Gateway stopped.${NC}"
    else
        echo -e "${RED}No running Api Gateway process found.${NC}"
    fi
}

case "$1" in
    run)
        run
        ;;
    stop)
        stop
        ;;
    restart)
        stop
        run
        ;;
    *)
        echo -e "${RED}Usage: $0 {run|stop|restart}${NC}"
        echo -e "  run     - Start the service"
        echo -e "  stop    - Stop the service"
        echo -e "  restart - Restart the service"
        exit 1
        ;;
esac
