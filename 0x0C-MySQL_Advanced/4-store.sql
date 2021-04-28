-- Creates a trigger to decrement quantity when order placed
CREATE TRIGGER decrement AFTER INSERT ON orders FOR EACH ROW UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
