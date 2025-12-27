c_bar = document.getElementById('bar');
        btnMenu = document.getElementById('menuToggle');


        btnMenu.addEventListener('click', () => {

            //alert('eu sou Buch');

            c_bar.classList.toggle('open');

            if (c_bar.classList.contains('open')) {

                btnMenu.classList.remove('fa-bars');
                btnMenu.classList.add('fa-times');

            }else{

                btnMenu.classList.remove('fa-times');
                btnMenu.classList.add('fa-bars');
                

            }
        });
        


const scrollBox = document.getElementById("myScroll");

  function scrollLeft() {
    scrollBox.scrollBy({ left: -220, behavior: 'smooth' });
  }

  function scrollRight() {
    scrollBox.scrollBy({ left: 220, behavior: 'smooth' });
  }

  // Scroll automático a cada 3 segundos
  setInterval(() => {
    scrollBox.scrollBy({ left: 220, behavior: 'smooth' });

    // Verifica se está no fim e volta ao início
    if (scrollBox.scrollLeft + scrollBox.clientWidth >= scrollBox.scrollWidth) {
      scrollBox.scrollTo({ left: 0, behavior: 'smooth' });
    }
  }, 3000); // tempo em milissegundos 
  






function loadProsseguirC() {


	const inDadoPesq = document.getElementById("inEmailH").value;
	
		
		fetch("/proceguirmail", {
			method: "POST",
			headers: {"Content-Type":"application/json"},
			body: JSON.stringify({
				indadopesq: inDadoPesq
			})
		
		
			})
			
			.then(response => response.json())
			.then(data => {
			
				if (data.redirect){
					//alert("larta do redirecionamento");
					window.location.href = data.redirect;
				
				}
				
				if (data.erro){
					//alert(data.erro);
					document.getElementById("notfyText").innerHTML = data.erro;
				
				}
				
			
			});
	
		
	
	
}









//Scroll Load Eventos E Comunicados

const cards = document.querySelectorAll('.box--card');
  let visibleCount = 4; // mostra 5 primeiro
  const step = 3; // mostra +3 a cada scroll
  const loader = document.getElementById('loader');

  // esconder todos após os primeiros 5
  cards.forEach((c, i) => {
    if (i >= visibleCount) c.classList.add('hidden');
  });

  // detectar scroll
  window.addEventListener('scroll', () => {
    const bottom = window.innerHeight + window.scrollY >= document.body.offsetHeight - 2;
    if (bottom) {
      loader.textContent = "Carregando mais...";
      setTimeout(() => {
        const hiddenCards = document.querySelectorAll('.box--card.hidden');
        for (let i = 0; i < step && i < hiddenCards.length; i++) {
          hiddenCards[i].classList.remove('hidden');
        }
        if (document.querySelectorAll('.box--card.hidden').length === 0) {
          loader.textContent = "Todos estão exibidos ✔️";
        }
      }, 500);
    }
  });

//and sccroll eventos e comunicados
		














//alert("ooooo");
botaoPC = document.getElementById("btnProceguirContate");

if (botaoPC){
	//alert("botao existe ...");
	botaoPC.addEventListener("click", loadProsseguirC);
}else{
	//print("botao nao existe");

}





function toggleDarkMode() {
  document.body.classList.toggle("dark-mode");

  const icon = document.querySelector(".btn-theme i");

  if (document.body.classList.contains("dark-mode")) {
    icon.classList.remove("fa-moon");
    icon.classList.add("fa-sun");
    localStorage.setItem("theme", "dark");
  } else {
    icon.classList.remove("fa-sun");
    icon.classList.add("fa-moon");
    localStorage.setItem("theme", "light");
  }
}

/* Manter preferência */
document.addEventListener("DOMContentLoaded", () => {
  const theme = localStorage.getItem("theme");
  const icon = document.querySelector(".btn-theme i");

  if (theme === "dark") {
    document.body.classList.add("dark-mode");
    icon.classList.remove("fa-moon");
    icon.classList.add("fa-sun");
  }
});




//hh

// faz a contagem de  visitas e usuarios 

// TOTAL DE VISITAS (sempre)
fetch('/countVisit', {
    method: 'POST'
});

// VISITANTE ÚNICO (1x por dia)
(function () {
    const hoje = new Date().toISOString().split('T')[0];
    const ultimaVisita = localStorage.getItem('ultima_visita');

    if (ultimaVisita !== hoje) {
        fetch('/newToday', { method: 'POST' })
            .then(res => {
                if (res.ok) {
                    localStorage.setItem('ultima_visita', hoje);
                }
            })
            .catch(() => {});
    }
})();


// fim da contagem