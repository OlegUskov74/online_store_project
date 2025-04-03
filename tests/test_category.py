def test_category_init(firs_product, second_product):
    assert firs_product.name == "Смартфоны"
    assert firs_product.description == "Смартфоны, как средство не только коммуникации"
    assert len(firs_product.products) == 2

    assert second_product.name == "Телевизоры"
    assert second_product.description == "Современный телевизор"
    assert len(second_product.products) == 3

    assert firs_product.category_count == 2
    assert second_product.category_count == 2

    assert firs_product.product_count == 5
    assert second_product.product_count == 5