class Player():
    Hand_Size = 0
    Deck_Size = 0
    Gy = 0
    Banishment = 0
    Monster_on_Field = 0
    Highest_Atk_on_Field = 0
    Backrow_on_Field = 0
    Face_up_Backrow = 0
    Total_Atk_on_Field = 0
    Life_Points = 8000
    Total_Cards = Hand_Size + Monster_on_Field + Backrow_on_Field

    def Increase_Hand_Size(self, count):
        self.Hand_Size = self.Hand_Size + count

    def Decrease_Hand_Size(self, count):
        self.Hand_Size = self.Hand_Size - count

    def Increase_Deck_Size(self, count):
        self.Deck_Size = self.Deck_Size + count

    def Decrease_Deck_Size(self, count):
        self.Deck_Size = self.Deck_Size - count

    def Increase_Gy(self, count):
        self.Gy = self.Gy + count

    def Decrease_Gy(self, count):
        self.Gy = self.Gy - count

    def Increase_Banishment(self, count):
        self.Banishment = self.Banishment + count

    def Decrease_Banishment(self, count):
        self.Banishment = self.Banishment - count

    def Increase_Monster_on_Field(self, count):
        self.Monster_on_Field = self.Monster_on_Field + count

    def Decrease_Monster_on_Field(self, count):
        self.Monster_on_Field = self.Monster_on_Field - count

    def New_Highest_Atk(self, new_atk):
        self.Highest_Atk_on_Field = new_atk

    def Increase_Backrow_on_Field(self, count):
        self.Backrow_on_Field = self.Backrow_on_Field + count

    def Decrease_Backrow_on_Field(self, count):
        self.Backrow_on_Field = self.Backrow_on_Field - count

    def Increase_Face_up_Backrow(self, count):
        self.Face_up_Backrow = self.Face_up_Backrow + count

    def Decrease_Face_up_Backrow(self, count):
        self.Face_up_Backrow = self.Face_up_Backrow - count

    def Change_Total_Atk_on_Field(self, new_atk):
        self.Total_Atk_on_Field = new_atk

    def Increase_Life_Points(self,count):
        self.Life_Points = self.Life_Points + count

    def Decrease_Life_Points(self, count):
        self.Life_Points = self.Life_Points - count

    def Change_Total_Cards(self):
        self.Total_Cards = self.Monster_on_Field + self.Hand_Size + self.Backrow_on_Field

    def set_Deck_Size(self,size):
        self.Deck_Size = size
