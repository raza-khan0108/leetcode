class ProductOfNumbers:

    def __init__(self):
        # The first 1 is a starting prefix product.
        self.prefix_products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Any product reaching across this zero is 0.
            # Start fresh for numbers added after it.
            self.prefix_products = [1]
        else:
            next_product = self.prefix_products[-1] * num
            self.prefix_products.append(next_product)

    def getProduct(self, k: int) -> int:
        # Fewer than k numbers since the latest zero means
        # the requested range contains a zero.
        if k >= len(self.prefix_products):
            return 0

        current_product = self.prefix_products[-1]
        product_before_last_k = self.prefix_products[-k - 1]

        return current_product // product_before_last_k