 KindEditor.options.filterMode = false;
        KindEditor.ready(function (K) {
            window.editor = K.create('#id_content',
                {
                    uploadJson: '/upload/',
                    width:'100%',
                    height:'1000px',
                    resizeType: 0,
                    extraFileUploadParams: {
                        csrfmiddlewaretoken: document.querySelector("[name='csrfmiddlewaretoken']").value
                    },
                }
            );
        });