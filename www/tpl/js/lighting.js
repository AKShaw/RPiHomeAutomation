function updateValue(){
	var status = 1;	
	if (toggleBtn.checked==true){
		status="1";
	}
	else if (toggleBtn.checked==false){
		status="0";
	}
	return status;
}

form.addEventListener('iron-form-presubmit', function() {
	//this.request.method = 'POST';
	var status = updateValue()
	this.request.params["onOff"] = status;
});
