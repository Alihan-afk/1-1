class UserProfile:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

    def __repr__(self):
        return f"UserProfile(name='{self.name}', email='{self.email}', role='{self.role}')"

# Мысал қолдану
user1 = UserProfile("Алихан", "alihan@example.com", "student")

# Өзгеріс енгізу үшін — жаңа объект жасаймыз
user2 = UserProfile(user1.name, "newmail@example.com", user1.role)

print(user1)
print(user2)




class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        """Векторларды қосу"""
        return Vector2D(self.x + other.x, self.y + other.y)

    def scale(self, factor):
        """Векторды масштабтау"""
        return Vector2D(self.x * factor, self.y * factor)

    def __repr__(self):
        return f"Vector2D(x={self.x}, y={self.y})"


# Мысал қолдану
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print(v1.add(v2))     # → Vector2D(x=4, y=6)
print(v1.scale(2))    # → Vector2D(x=6, y=8)




class FrozenInvoice:
    def __init__(self, price, quantity):
        self._price = price
        self._quantity = quantity

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    @property
    def total(self):
        return self._price * self._quantity

    def __repr__(self):
        return f"FrozenInvoice(price={self.price}, quantity={self.quantity}, total={self.total})"


# Мысал қолдану
invoice = FrozenInvoice(500, 3)
print(invoice.total)  # → 1500
