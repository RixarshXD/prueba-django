from django.shortcuts import render

# Create your views here.

def renderIndex(request):
    data = {
        'contexto' : 'guitarras',
        'btn_guitarras' : 'Guitarras',
        'btn_cuerdas' : 'Cuerdas',
        'btn_maderas' : 'Maderas'
    } 

    return render(request, 'App1/index.html', data)



def renderContexto(request, categoria):
    productos ={
        'Guitarras' : ['guitarra1','guitarra2','guitarra3'],
        'Cuerdas' : ['cuerdas1','cuerdas2','cuerdas3'],
        'Maderas' : ['madera1','madera2','madera3']       
    }

    categoria = {
        'categoria' : categoria,
        'elementos' : productos.get(categoria,[])
    }

    return render(request,'App1/contexto.html', categoria)