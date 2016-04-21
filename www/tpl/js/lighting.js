
status=1;

function updateValue(){
	if (toggleBtn.checked()==true){
		status=1;
	}
	else if (toggleBtn.checked()==false){
		status=0;
	}
}

form.addEventListener('iron-form-presubmit', function() {
	this.request.method = 'put';
	this.request.params = ["onOff", status];
});
