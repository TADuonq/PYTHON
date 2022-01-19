import os

import tensorflow_datasets.public_api as tfds

_CITATION = """
@ONLINE {tfflowers,
author = "The TensorFlow Team",
title = "Flowers",
month = "jan",
year = "2019",
url = "http://download.tensorflow.org/example_images/flower_photos.tgz" }
"""

_URL = "http://download.tensorflow.org/example_images/flower_photos.tgz"


class TFFlowers(tfds.core.GeneratorBasedBuilder):
  """Flowers dataset."""

  VERSION = tfds.core.Version("3.0.1")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description="A large set of images of flowers",
        features=tfds.features.FeaturesDict({
            "image":
                tfds.features.Image(),
            "label":
                tfds.features.ClassLabel(names=[
                    "dandelion", "daisy", "tulips", "sunflowers", "roses"
                ]),
        }),
        supervised_keys=("image", "label"),
        homepage="https://www.tensorflow.org/tutorials/load_data/images",
        citation=_CITATION)

  def _split_generators(self, dl_manager):
    path = dl_manager.download(_URL)

    # There is no predefined train/val/test split for this dataset.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"images_dir_path": dl_manager.iter_archive(path)}),
    ]

  def _generate_examples(self, images_dir_path):
    """Generate flower images and labels given the image directory path.
    Args:
      images_dir_path: path to the directory where the images are stored.
    Yields:
      The image path and its corresponding label.
    """
    for fname, fobj in images_dir_path:
      if fname.endswith(".jpg"):
        image_dir, image_file = os.path.split(fname)
        d = os.path.basename(image_dir)
        record = {"image": fobj, "label": d.lower()}
        yield "%s/%s" % (d, image_file), record