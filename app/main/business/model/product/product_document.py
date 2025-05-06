from sqlalchemy import BigInteger, Boolean, Column, ForeignKey
from .....extensions import db
from ....utils.model.common_model import CommonModel
from flask_restx import fields
from sqlalchemy.orm import relationship


class ProductDocument(CommonModel, db.Model):
    __tablename__ = "product_document_master"
    id = Column(BigInteger(), primary_key=True)
    document_id = Column(BigInteger, ForeignKey("document_master.id"), nullable=True)
    product_id = Column(BigInteger, ForeignKey("product_master.id"), nullable=True)
    document = relationship(
        "DocumentMaster", foreign_keys=[document_id], backref="product_document"
    )
    product = relationship(
        "ProductMaster", foreign_keys=[product_id], backref="document_as_product"
    )
    is_default = Column(Boolean, nullable=True, default=False)

    @property
    def file_path(self):
        return self.document.file_path if self.document is not None else None

    def save(self):
        db.session.add(self)
        db.session.commit()
