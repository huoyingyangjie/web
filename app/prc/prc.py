class PrcItem:
    def __init__(self,name,value="",display=False,edit=False,edit_type="checkbox"):
        self.name=name;
        self.value=value;
        self.display=display;
        self.edit=edit;
        self.edit_type=edit_type;
        assert not (display==False and edit==True)