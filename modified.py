def register(request):
    if request.method=='POST':
        form=NewUserForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            print('Yes')
            messages.success(request,'registration sucessful')
            return redirect('signin')
        else:
            print('no')
        return render(request,'signup.html',{'form':form})
    
    else:
        form= NewUserForm()
        return render(request,'signup.html',{'form':form})
