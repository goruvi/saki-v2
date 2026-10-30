import discord
from discord.ext import commands


class EditMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(
        name="editmessage",
        description="Sửa một tin nhắn do bot gửi"
    )
    @discord.app_commands.describe(
        message_id="ID của tin nhắn cần sửa",
        new_content="Nội dung mới"
    )
    async def editmessage(
        self,
        interaction: discord.Interaction,
        message_id: str,
        new_content: str
    ):
        # Chỉ Admin
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
                "❌ Chỉ Admin mới có thể sử dụng lệnh này.",
                ephemeral=True
            )
            return

        # Kiểm tra Message ID
        try:
            message_id = int(message_id)
        except ValueError:
            await interaction.response.send_message(
                "❌ Message ID không hợp lệ.",
                ephemeral=True
            )
            return

        await interaction.response.defer(ephemeral=True)

        message = None

        # Tìm message trong các text channel
        for channel in interaction.guild.text_channels:
            try:
                found = await channel.fetch_message(message_id)

                if found:
                    message = found
                    break

            except discord.NotFound:
                continue

            except discord.Forbidden:
                continue

            except discord.HTTPException:
                continue

        # Không tìm thấy
        if message is None:
            await interaction.followup.send(
                "❌ Không tìm thấy tin nhắn.",
                ephemeral=True
            )
            return

        # Chỉ cho sửa message của bot
        if message.author.id != self.bot.user.id:
            await interaction.followup.send(
                "❌ Bạn chỉ có thể sửa tin nhắn do bot gửi.",
                ephemeral=True
            )
            return

        try:
            await message.edit(content=new_content)

            await interaction.followup.send(
                "✅ Đã sửa tin nhắn thành công!",
                ephemeral=True
            )

        except discord.Forbidden:
            await interaction.followup.send(
                "❌ Bot không có quyền sửa tin nhắn này.",
                ephemeral=True
            )

        except discord.HTTPException as e:
            await interaction.followup.send(
                f"❌ Không thể sửa tin nhắn.\n`{e}`",
                ephemeral=True
            )


async def setup(bot):
    await bot.add_cog(EditMessage(bot))