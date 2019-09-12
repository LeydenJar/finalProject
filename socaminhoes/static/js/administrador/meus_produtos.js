document.addEventListener('DOMContentLoaded', ()=>{
	document.querySelectorAll('.botão_excluir').forEach(function(botao){
		botao.onclick = ()=>{
			const pk = botao.getAttribute('data-pk');
			console.log(pk);
			var formulario = document.getElementById('formulario_deletar_item');
			var form = new FormData(formulario);
			form.append('pk', pk);
			var request = new XMLHttpRequest;
			request.open('POST', 'excluir_produto');
			request.send(form);
			request.onload = ()=>{
				if(request.status === 200){
					location.reload();
				}else{alert('error');}
			}
		}
	});
});
