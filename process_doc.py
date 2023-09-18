from typing import List

from dotenv import load_dotenv
from instructor import openai_schema
from pydantic import create_model

load_dotenv()


def create_schema_model(fields, field_name="Document"):
    labels = [i.strip() for i in fields.split(",")]
    model = openai_schema(
        create_model(field_name, **{item: (type(item), ...) for item in labels})
    )
    multi_model = openai_schema(create_model(f"{field_name}s", data=(List[model], ...)))
    return multi_model
