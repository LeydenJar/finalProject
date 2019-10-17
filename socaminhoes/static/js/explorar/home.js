document.addEventListener("DOMContentLoaded", function(){
	var divs_produtos = document.querySelectorAll('.div_do_produto');
	divs_produtos.forEach(function(div){
		div.onclick = ()=>{
			pk = div.getAttribute('data-produto');
			window.location.assign('/caminhao/' + pk);

		}
	});

	var navbar = document.querySelector('#navbar_responsiva');
	var hamburguer = document.querySelector('#hamburguer');

	hamburguer.onclick = ()=>{
		if (navbar.classList.contains('collapse')){
			navbar.classList.remove('collapse');
		}else{
			navbar.classList.add('collapse');
		}
	}
});