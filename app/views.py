from django.shortcuts import render

def index(request):
    return render (request, "index.html")

def atletas(request):
    atletas = [
        {"Nome": "Lara Nobre Cardoso", "idade": "34", 
         "Posição": "Central", 
         "Nascimento": "São Paulo, SP", 
         "foto": "img/lara.cardoso.jpg"},

         {"Nome": "Diana Duarte", "idade": "25", 
         "Posição": "Central", 
         "Nascimento": "Barueri, SP", 
         "foto": "img/diana duarte.jpg"},

         {"Nome": "Nyeme Costa Nunes", "idade": "25", 
         "Posição": "Líbero", 
         "Nascimento": "Barra do Corda, MA", 
         "foto": "img/nyeme.costa.jpg"},

         {"Nome": "Lorena Viezel", "idade": "25", 
         "Posição": "Central", 
         "Nascimento": "Ponta Porã, MS", 
         "foto": "img/lorena-viezel.jpg"},

         {"Nome": "Priscila Daroit", "idade": "35", 
         "Posição": "Ponta", 
         "Nascimento": "Porto Alegre, RS", 
         "foto": "img/priscila.daroit.jpg"},

         {"Nome": "Thaisa Daher de Menezes", "idade": "37", 
         "Posição": "Central", 
         "Nascimento": "Rio de Janeira,RJ", 
         "foto": "img/thaisa.daher.jpg"},

          {"Nome": "Rosamaria Montibeller", "idade": "30", 
         "Posição": "Oposta/Ponta", 
         "Nascimento": "Nova Trento, SC", 
         "foto": "img/rosamaria.montibeller.jpg"},

          {"Nome": "Macris Carneiro", "idade": "35", 
         "Posição": "Levantadora", 
         "Nascimento": "Santo André, SP", 
         "foto": "img/macris.carneiro.jpg"},

          {"Nome": "Roberta Ratzke", "idade": "34", 
         "Posição":"Levantadora", 
         "Nascimento": "Curitiba, PR", 
         "foto": "img/roberta.ratkze.jpg"},

          {"Nome": "Gabriela Guimarães", "idade": "30", 
         "Posição": "Ponta", 
         "Nascimento": "Belo Horizonte, MG", 
         "foto": "img/gabriela.guimaraes.jpg"},

          {"Nome": "Maiara Basso", "idade": "28", 
         "Posição": "Ponta", 
         "Nascimento": "Palotina, PR", 
         "foto": "img/maiara.basso.jpg"},

          {"Nome": "Ana Cristina", "idade": "20", 
         "Posição": "Ponta", 
         "Nascimento": "Rio de Janeira,RJ", 
         "foto": "img/ana.cristina.jpg"},

          {"Nome": "Natália Pereira de Araújo ", "idade": "27", 
         "Posição": "Líbero", 
         "Nascimento": "Guarulhos, SP", 
         "foto": "img/natalia.pereira.jpg"},

          {"Nome": "Ana Carolina", "idade": "33", 
         "Posição": "Central", 
         "Nascimento": "Belo Horizonte, MG", 
         "foto": "img/ana.carolina.jpg"},

          {"Nome": "Kisy Nascimento", "idade": "24", 
         "Posição": "Oposta", 
         "Nascimento": "São Paulo,SP", 
         "foto": "img/kisy.nascimento.jpg"},

          {"Nome": "Julia Bergmann", "idade": "23", 
         "Posição": "Ponta", 
         "Nascimento": "Munique, Alemanha", 
         "foto": "img/julia.bergmann.jpg"},

          {"Nome": "Tainara Santos", "idade": "25", 
         "Posição":"Oposta", 
         "Nascimento": "Jandira, SP", 
         "foto": "img/tainara.santos.jpg"},

          {"Nome": "Lorrayna Marys", "idade": "25", 
         "Posição": "Oposta", 
         "Nascimento": "Taubaté, SP", 
         "foto": "img/lorrayna.marys.jpg"},

          {"Nome": "Naiane Rios", "idade": "29", 
         "Posição": "Levantadora", 
         "Nascimento": "Belém,PA", 
         "foto": "img/naiane.jpg"},

          {"Nome": "Lorenne Geraldo", "idade": "28", 
         "Posição": "Oposta", 
         "Nascimento": "Conselheiro Lafaiate, MG", 
         "foto": "img/lorene.geraldo.jpg"},    
    ]

    context = {
        "atletas": atletas,
    }
    return render(request, "atletas.html", context)

def sobre(request):
    return render(request, "sobre.html")