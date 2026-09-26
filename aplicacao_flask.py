from flask import Flask, render_template, request, redirect,
url_for
chamado = conexao.execute(
"SELECT * FROM chamados WHERE id = ?",
(id,)
).fetchone()conexao.close()
if chamado is None:
return "Chamado não encontrado", 404
return render_template(
"chamado.html",
chamado=chamado
)
@app.route("/chamados/<int:id>/status", methods=["POST"])
def alterar_status(id):
status = request.form["status"]
conexao = conectar()
conexao.execute(
"""
UPDATE chamados
SET status = ?
WHERE id = ?
""",
(status, id)
)
conexao.commit()
conexao.close()
return redirect(
url_for("visualizar_chamado", id=id)
)
@app.route("/chamados/<int:id>/excluir", methods=["POST"])
def excluir_chamado(id):
conexao = conectar()
conexao.execute(
"DELETE FROM chamados WHERE id = ?",
(id,)
)
conexao.commit()
conexao.close()
return redirect(url_for("listar_chamados"))
if __name__ == "__main__":
app.run(debug=True)