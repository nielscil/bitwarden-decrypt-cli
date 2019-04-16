import pytest
from bitwarden_decrypt_simple_cli.services.CryptoService import CryptoService
from bitwarden_decrypt_simple_cli.models.domain.SymmetricCryptoKey import SymmetricCryptoKey
from bitwarden_decrypt_simple_cli.tests.fixtures_common import bw_session, crypto_service

@pytest.mark.usefixtures("bw_session")
def test_has_key(crypto_service: CryptoService):
    assert crypto_service.has_key() == True


@pytest.mark.usefixtures("bw_session")
def test_get_key(crypto_service: CryptoService):
    key= crypto_service.get_key()
    assert key is not None
    assert isinstance(key, SymmetricCryptoKey)
    assert key.encType.value == 0
    assert key.keyB64 == b'/lCGAMDGAq+mjRP3FJv+VNDDnbrYcVGnsiPeXTm4NfU='
    assert key.encKeyB64 == b'/lCGAMDGAq+mjRP3FJv+VNDDnbrYcVGnsiPeXTm4NfU='