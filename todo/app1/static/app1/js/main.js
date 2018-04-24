
			$('input:checkbox').change(function () {
 
			var chkbx= $(this);
			var parent=chkbx.parent();
			var chbxid = $(this).val();
            var check = $(this).attr('checked');
			
            $.ajax({ 
			type:'POST',
			url:'/update',
			data:{
			id:chbxid,
			val:check,
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
			},
			success:function(){
			if (chkbx.is(':checked'))			
			{
			parent.addClass('completed')
			}
			else { parent.removeClass('completed');}
			}
			})
        });
		
		$('i').click(function() {
			btn=$(this);
			
			btn_id=btn.attr('id');
			console.log(btn.id);
		            $.ajax({ 
			type:'POST',
			url:'/delrow',
			data:{
			id:btn_id,
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
			},
			success:function(){
			location.reload();
			}
			})
		
		
		})