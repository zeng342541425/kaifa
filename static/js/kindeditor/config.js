KindEditor.ready(function (k) {
    window.editor = k.create('#id_content',{
        resizeType:1,
        allowPreviewEmoticons : false,
        allowImageRemote : false,
        uploadJson : '/admin/upload/kindeditor',
        width:'800px',
        height:'400px',
 
    });
})
