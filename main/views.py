from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .what_auto import send_whatsapp_message
from django.templatetags.static import static

class Auto(View):
    def post(self, request, *args, **kwargs):
        try:
            msg=request.POST.get("msg")
            files=request.FILES.get("file")
            print(type(files))
            print(type(msg))

            for line in files:
                line = line.decode('utf-8').strip()
                send_whatsapp_message(line,msg)
            else:
                Response='''
                    <p>Mesasge has been sent</p>
                    <button hx-target=#form-target hx-get="/Auto_page" type="submit" class="bg-blue-500 hover:bg-blue-700 text-white justify-center font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Go back</button>
                '''
                return httpresponse(Response)
      
        except Exception as e:
            Response='''
                <p>The message  has been sent!!!</p>
                <p>Wanna send anther one?</p>
                <div>
                    <div class="w-full"></div>
                    <div class="w-full h-72"></div>
                    <div class="flex items-center justify-center">
                        <button hx-target=#form-target hx-get="/Auto_page" type="submit" class="bg-blue-500 hover:bg-blue-700 text-white justify-center font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Go back</button>
                    </div>
                </div>
            '''
            return HttpResponse(Response)
        

        return render(request, "result.html", {"status": "invalid_request"})

    def get(self, request, *args, **kwargs):
        return render(request, "index.html")

def home(request):
    return render(request, "home.html")

# Initialize the global variables
message = [
            'Hi there fellas, venti here!! I made an easy way to send messages to your freinds out there!!!',
            'fill in these two boxes to send your messages to multiple people', 
            'You put the message to send here', 
            'Upload your file here!!',
            'Now go annoy your freinds with your dumb messages'
        ]
img_url = ['images/venti_pg_1.jpg',
           'images/venti_pg1.1.png', 
           'images/Designer_1.png', 
           'images/Designer_2.png', 
           'images/venti_pg5.jpg']
i = 0

def next_message(request):
    global i
    i += 1
    if i >= 5:
        i = 4

    arrow='images/right-arrow-angle.png'
    arrow_L='images/left-arrow-angle.png'
    print(i)
    if i == 4:
        context = f'''
            <a id="button-target" hx-get="/Auto_page" class="absolute bottom-36 right-96 flex items-center">
                <img id="arrow-target" src="{static(arrow)}" alt="Icon" class="w-10 h-10 mr-2">
            </a>
            <a hx-get="/prev" hx-target="#target-container" class="absolute bottom-36 left-96 flex items-center">
                <img src="{static(arrow_L)}" alt="Icon" class="w-10 h-10 mr-2">
            </a>  
            <div id="info-target" class="grid grid-col-2 gap-4 mt-4">
                <div class="flex justify-center">
                    <p id="paragraph-target">{message[i]}</p>
                </div>
                <div class="flex justify-center">
                    <img class="w-36 h-36" src="{static(img_url[i])}" alt="Image" id="image-target">
                </div>
                    
            </div>
        '''   
    elif i==1:
        context = f'''
            <a id="button-target" hx-get="/next" hx-target="#target-container" class="absolute bottom-36 right-96 flex items-center">
                <img id="arrow-target" src="{static(arrow)}" alt="Icon" class="w-10 h-10 mr-2">
            </a>
            <a hx-get="/prev" hx-target="#target-container" class="absolute bottom-36 left-96 flex items-center">
                <img src="{static(arrow_L)}" alt="Icon" class="w-10 h-10 mr-2">
            </a>
            <div id="info-target" class="grid grid-col-2 gap-4 mt-4">
                <div class="flex justify-center">
                    <p id="paragraph-target">{message[i]}</p>
                </div>
                <div class="flex justify-center">
                    <img class="w-64 h-64" src="{static(img_url[i])}" alt="Image" id="image-target">
                </div>
                    
            </div>   
        '''   
    elif i==2:
        context = f'''
            <a id="button-target" hx-get="/next" hx-target="#target-container" class="absolute bottom-36 right-96 flex items-center">
                <img id="arrow-target" src="{static(arrow)}" alt="Icon" class="w-10 h-10 mr-2">
            </a>
            <a hx-get="/prev" hx-target="#target-container" class="absolute bottom-36 left-96 flex items-center">
                <img src="{static(arrow_L)}" alt="Icon" class="w-10 h-10 mr-2">
            </a>
            <div id="info-target" class="grid grid-col-2 gap-4 mt-4">
                <div class="flex justify-center">
                    <p id="paragraph-target">{message[i]}</p>
                </div>
                <div class="flex justify-center">
                    <img class="w-64 h-48" src="{static(img_url[i])}" alt="Image" id="image-target">
                </div>
                    
            </div>   
        '''   
    elif i==3:
        context = f'''
            <a id="button-target" hx-get="/next" hx-target="#target-container" class="absolute bottom-36 right-96 flex items-center">
                <img id="arrow-target" src="{static(arrow)}" alt="Icon" class="w-10 h-10 mr-2">
            </a>
            <a hx-get="/prev" hx-target="#target-container" class="absolute bottom-36 left-96 flex items-center">
                <img src="{static(arrow_L)}" alt="Icon" class="w-10 h-10 mr-2">
            </a>
            <div id="info-target" class="grid grid-col-2 gap-4 mt-4">
                <div class="flex justify-center">
                    <p id="paragraph-target">{message[i]}</p>
                </div>
                <div class="flex justify-center">
                    <img class="w-64 h-48" src="{static(img_url[i])}" alt="Image" id="image-target">
                </div>
                    
            </div>   
        '''               
    else:
        context = f'''
            <a id="button-target" hx-get="/next" hx-target="#target-container" class="absolute bottom-36 right-96 flex items-center">
                <img id="arrow-target" src="{static(arrow)}" alt="Icon" class="w-10 h-10 mr-2">
            </a>
            <a hx-get="/prev" hx-target="#target-container" class="absolute bottom-36 left-96 flex items-center">
                <img src="{static(arrow_L)}" alt="Icon" class="w-10 h-10 mr-2">
            </a>
            <div id="info-target" class="grid grid-col-2 gap-4 mt-4">
                <div class="flex justify-center">
                    <p id="paragraph-target">{message[i]}</p>
                </div>
                <div class="flex justify-center">
                    <img class="w-36 h-36" src="{static(img_url[i])}" alt="Image" id="image-target">
                </div>
                    
            </div>   
        '''
    return HttpResponse(context)

def Auto_page(request):
    response = HttpResponse()
    response['HX-Location'] = '/Auto/'  # Replace with the URL you want to redirect to
    return response

def prev_message(request):
    global i
    i -= 1
    if i < 0:
        i = 0
    
    arrow='images/right-arrow-angle.png'
    arrow_L='images/left-arrow-angle.png' 
    img_src = static(img_url[i])
    if i == 0 or i == 4:
        context =  f'''
            <a id="button-target" hx-get="/next" hx-target="#target-container" class="absolute bottom-36 right-96 flex items-center">
                <img id="arrow-target" src="{static(arrow)}" alt="Icon" class="w-10 h-10 mr-2">
            </a>
            <a hx-get="/prev" hx-target="#target-container" class="absolute bottom-36 left-96 flex items-center">
                <img src="{static(arrow_L)}" alt="Icon" class="w-10 h-10 mr-2">
            </a>  
            <div id="info-target" class="grid grid-col-2 gap-4 mt-4">
                <div class="flex justify-center">
                    <p id="paragraph-target">{message[i]}</p>
                </div>
                <div class="flex justify-center">
                    <img class="w-36 h-36" src="{static(img_url[i])}" alt="Image" id="image-target">
                </div>            
            </div> 
        '''
    else:
        context =  f'''
            <a id="button-target" hx-get="/next" hx-target="#target-container" class="absolute bottom-36 right-96 flex items-center">
                <img id="arrow-target" src="{static(arrow)}" alt="Icon" class="w-10 h-10 mr-2">
            </a>
            <a hx-get="/prev" hx-target="#target-container" class="absolute bottom-36 left-96 flex items-center">
                <img src="{static(arrow_L)}" alt="Icon" class="w-10 h-10 mr-2">
            </a>  
            <div id="info-target" class="grid grid-col-2 gap-4 mt-4">
                <div class="flex justify-center">
                    <p id="paragraph-target">{message[i]}</p>
                </div>
                <div class="flex justify-center">
                    <img class="w-64 h-48" src="{static(img_url[i])}" alt="Image" id="image-target">
                </div>            
            </div> 
        '''
       
    return HttpResponse(context)


def buffer(request):
    return render(request,"test.html")