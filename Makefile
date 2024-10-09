ui_install:
	cd frontend && bun i

ui_dev:
	cd frontend && bun run dev

tlsn_server:
	cd backend/tlsn/tlsn/examples && cargo run --bin simple_prover

regression_server:
	cd backend/regression && python app.py