#!/bin/bash
set -e

prometheus_url=http://localhost:9090

echo "Plotting it"
promplot -url $prometheus_url \
  -range '10m' \
  -title "CPU_USAGE" \
  -query "sum(rate(container_cpu_usage_seconds_total{name='python'}[15s])) by (name)" \
  -file $1/cpu.png

promplot -url $prometheus_url \
  -range '10m' \
  -title "MemoryUsage" \
  -query "MIN(container_memory_usage_bytes{name='python'}/1024) by (name)" \
  -file $1/memory.png
