resource "azurerm_network_interface" "test" {
  name                = "${var.resource_type}-${var.application_type}-nic"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${var.subnet_id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "${var.public_ip_address_id}"
  }
}

resource "azurerm_linux_virtual_machine" "test" {
  name                = "${var.resource_type}-${var.application_type}-vm"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  size                = "Standard_DS2_v2"
  admin_username      = "${var.vm_admin_username}"
  admin_password = "${var.vm_password}"
  network_interface_ids = [azurerm_network_interface.test.id]
  admin_ssh_key {
    username   = "${var.vm_admin_username}"
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC7qr08p7822iNxkU0t/p17M1oqHVua0vEMJ93HU2deJJGg6bS6QtLLQ2bKpkHq547w0BBevePlyvhN5UEOPKThjn9yRrZiRMvmS6v1GEVY/bUHpDvWXwwN/tQi8casDswSVDsuCyP+0gLZI5S5eCwTYFQvKl/FBe+s5SBNwCjGDPnwHHhu79LtGgbUTYozbt0JVavprYStZ7+Xxa343g1rVKHxgZl5Vpe0m8Pggby5o4L5kjQcn37GfLwPn5NV9VXLOobH1fxMyiDnTEMze61fWu8Iqp4blt/GQnulyldgHxV3zw5I2ZBrqcKX4WkKyF1wWxqf7AMxJZInc877b5hn mgorkii@NLP-LT83"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
