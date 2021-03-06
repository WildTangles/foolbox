import pytest
import numpy as np

from foolbox.v1.attacks import AdditiveUniformNoiseAttack
from foolbox.v1.attacks import AdditiveGaussianNoiseAttack
from foolbox.v1.attacks import SaltAndPepperNoiseAttack
from foolbox.v1.attacks import BlendedUniformNoiseAttack

Attacks = [
    AdditiveUniformNoiseAttack,
    AdditiveGaussianNoiseAttack,
    SaltAndPepperNoiseAttack,
    BlendedUniformNoiseAttack,
]


@pytest.mark.parametrize("Attack", Attacks)
def test_attack(Attack, bn_adversarial):
    adv = bn_adversarial
    attack = Attack()
    attack(adv)
    assert adv.perturbed is not None
    assert adv.distance.value < np.inf


@pytest.mark.parametrize("Attack", Attacks)
def test_attack_gl(Attack, gl_bn_adversarial):
    adv = gl_bn_adversarial
    attack = Attack()
    attack(adv)
    assert adv.perturbed is not None
    assert adv.distance.value < np.inf


@pytest.mark.parametrize("Attack", Attacks)
def test_attack_impossible(Attack, bn_impossible):
    adv = bn_impossible
    attack = Attack()
    attack(adv)
    assert adv.perturbed is None
    assert adv.distance.value == np.inf
