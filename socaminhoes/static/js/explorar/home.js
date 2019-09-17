document.addEventListener("DOMContentLoaded", function(){
	var divs_produtos = document.querySelectorAll('.div_do_produto');
	divs_produtos.forEach(function(div){
		div.onclick = ()=>{
			pk = div.getAttribute('data-produto');
			window.location.assign('/caminhao/' + pk);

		}
	});
});