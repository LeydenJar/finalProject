/*document.addEventListener('DOMContentLoaded', function(){
	botão_enviar = document.getElementById('botão_enviar');
	formulario = document.getElementById('formulario');
	form_titulo = document.getElementById('id_titulo');
	form_preço = document.getElementById('id_preço');
	form_imagem = document.getElementById('id_imagem');
	botão_enviar.onclick = ()=>{
		data = newFormData(formulario);
		data.append('titulo', form_titulo.value);
		data.append('preço', form_preço.value);
		data.append('imagem', form_imagem.files[0]);
		request = new XMLHttpRequest;
		request.open('POST', 'admin/novo_produto');
		request.send(data);
		request.onload = ()=>{
			if (request.status === 200){
				location.reload();
			}else{
				alert("error!");
			}
		}
		return false

	}
});*/