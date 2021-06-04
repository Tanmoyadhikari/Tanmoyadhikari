
		function calcu (x) {
			
			form.display.value = form.display.value + x;
		};
		
		
		function date () {
			
			var set= new Date();
			var hour= set.getHours();
			var min= set.getMinutes();
			var sec= set.getSeconds();
			var milsec= set.getMilliseconds();
			
			
			var main= hour +":"+min+":"+sec+":"+milsec;
			
			
			
			document.getElementById("time").innerHTML= " <b> <u>The Time Is:</u></b> "+ main;
			
			
			setInterval(date,1000);
			
		}
		
		